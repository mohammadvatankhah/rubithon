from .rpc_error import RPCError


class ForbiddenError(RPCError):
    name = "Forbidden"
    status = "INVALID_ACCESS"
