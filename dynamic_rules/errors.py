class TypeNotSupportedError(Exception):
    def __init__(self, message=None):
        self.message = message or "Instance type not supported"


class DataTypeMismatchError(Exception):
    def __init__(self, message):
        self.message = message or "Data type mismatch between rule and input parameter"
