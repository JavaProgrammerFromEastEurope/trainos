class MetaCycle:

    def __init__(self) -> None:
        self.tick_index = 0

    def tick(self) -> int:
        self.tick_index += 1
        return self.tick_index
