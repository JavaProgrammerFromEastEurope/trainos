from .validator import Validator


class ValidationEngine:

    def __init__(self):
        self.validator = Validator()

    def validate(self, value, rule):
        return self.validator.validate(value, rule)
