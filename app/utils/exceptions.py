class ValidationError(Exception):
    def __init__(self, field, reason):
        self.field = field
        self.reason = reason
        super().__init__(reason)


class NotFoundError(Exception):
    def __init__(self, reason, field="id"):
        self.field = field
        self.reason = reason
        super().__init__(reason)
