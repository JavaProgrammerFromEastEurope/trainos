class SystemState:

    def __init__(self):

        self.state: dict = {}

    def set(self, key: str, value):

        self.state[key] = value

    def get(self, key: str):

        return self.state.get(key)

    def export(self):

        return self.state
