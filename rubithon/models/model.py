from copy import copy
from enum import Enum
from inspect import isclass
from json import dumps
from typing import Optional, Union, get_args, get_origin, get_type_hints

import rubithon


class Model:
    attribute_names = []

    @classmethod
    def expected_types(cls):
        return get_type_hints(cls.__init__)

    @classmethod
    def validate_types(cls, raw_model):
        expected_types = cls.expected_types()
        for key, value in list(raw_model.items()):
            if key not in expected_types or value is None:
                continue
            expected_type = expected_types[key]
            if get_origin(expected_type) is Union:
                arguments = get_args(expected_type)
                actual_types = [arg for arg in arguments if arg is not type(None)]
                if actual_types:
                    expected_type = actual_types[0]

            if get_origin(expected_type) is list:
                if isinstance(value, list):
                    raw_model[key] = wrap(expected_type, value)
                continue

            if isclass(expected_type) and issubclass(expected_type, Enum):
                if not isinstance(value, expected_type):
                    try:
                        raw_model[key] = expected_type(value)
                    except (ValueError, TypeError):
                        pass
                continue

            if not (isclass(expected_type) and issubclass(expected_type, Model)):
                continue

            if not isinstance(value, expected_type):
                raw_model[key] = expected_type.wrap(value)

        return raw_model

    @classmethod
    def wrap(cls, raw_model):
        if isinstance(raw_model, dict) and len(raw_model) == 1:
            key, value = next(iter(raw_model.items()))
            allowed_keys = {
                attribute if isinstance(attribute, str) else attribute[1]
                for attribute in cls.attribute_names
            }
            if key not in allowed_keys and isinstance(value, dict):
                raw_model = value

        for attribute_name, key_name in cls.attribute_names:
            if raw_model.get(key_name):
                raw_model[attribute_name] = raw_model.pop(key_name)

        raw_model = cls.validate_types(raw_model)
        return cls(**raw_model)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def bind(self, client):
        self.client = client
        for value in self.__dict__.values():
            if isinstance(value, Model):
                value.bind(client)

    def __init__(self, **keyword_arguments):
        self.client: Optional["rubithon.Client"] = None
        for key, value in keyword_arguments.items():
            self[key] = value

    def unwrap(self):
        result = copy(self)
        del result.client

        for key, value in list(result.__dict__.items()):
            if isinstance(value, Enum):
                result[key] = value.value
            elif isinstance(value, list):
                result[key] = unwrap(value)
            elif isinstance(value, Model):
                result[key] = value.unwrap()
            elif value is None:
                delattr(result, key)

        for attribute_name, key_name in self.attribute_names:
            if getattr(result, attribute_name, None):
                setattr(result, key_name, getattr(result, attribute_name))
                delattr(result, attribute_name)

        return result.__dict__

    def to_json(self):
        return dumps(self.unwrap(), ensure_ascii=False, indent=4)

    def __repr__(self):
        attributes_list = []
        for key, value in self.__dict__.items():
            if key == "client" or value is None:
                continue
            attributes_list.append(f"{key}={repr(value)}")

        if not attributes_list:
            return f"{type(self).__name__}()"

        attributes_list = ",\n".join(attributes_list)
        attributes_list = "\n".join(" " * 4 + line for line in attributes_list.splitlines())
        return f"{type(self).__name__}(\n{attributes_list}\n)"


def wrap(expected_type, raw_model):
    if get_origin(expected_type) is list and isinstance(raw_model, dict):
        for value in raw_model.values():
            if isinstance(value, list):
                raw_model = value
                break

    if get_origin(expected_type) is list:
        if isinstance(raw_model, list):
            item_type = get_args(expected_type)[0]
            raw_model = copy(raw_model)

            for index, element in enumerate(raw_model):
                if element is None:
                    continue
                if get_origin(item_type) is list:
                    if isinstance(element, list):
                        raw_model[index] = wrap(item_type, element)
                    continue
                if not (isclass(item_type) and issubclass(item_type, Model)):
                    continue
                if not isinstance(element, item_type):
                    raw_model[index] = item_type.wrap(element)

            from .list import List as RubithonList
            return RubithonList(raw_model)

    if isclass(expected_type) and issubclass(expected_type, Model):
        return expected_type.wrap(raw_model)

    return raw_model


def unwrap(wrapped):
    if isinstance(wrapped, list):
        wrapped = copy(wrapped)
        for index, element in enumerate(wrapped):
            wrapped[index] = unwrap(element)
        return list(wrapped)

    if isinstance(wrapped, Model):
        return wrapped.unwrap()

    if isinstance(wrapped, Enum):
        return wrapped.value

    return wrapped
