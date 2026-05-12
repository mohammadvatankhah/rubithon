from .model import Model, unwrap


class List(list, Model):
    @classmethod
    def wrap(cls, raw_model):
        return cls(raw_model)

    def bind(self, client):
        self.client = client
        for element in self:
            if isinstance(element, Model):
                element.bind(client)

    def unwrap(self):
        return unwrap(self)

    def __repr__(self):
        if not self:
            return "[]"
        elements = ",\n".join(f"{repr(element)}" for element in self)
        elements = "\n".join(" " * 4 + line for line in elements.splitlines())
        return f"[\n{elements}\n]"
