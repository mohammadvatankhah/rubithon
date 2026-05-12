from .rpc_error import RPCError


class BadRequestError(RPCError):
    name = "Bad Request"
    status = "INVALID_INPUT"
