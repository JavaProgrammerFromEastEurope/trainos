from .default_provider import DefaultProvider


class ProviderEngine:

    def __init__(self):
        self.provider = DefaultProvider()

    def load(self, value):
        return self.provider.load(value)
