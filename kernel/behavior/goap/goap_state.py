from dataclasses import dataclass


@dataclass
class GOAPState:

    values: dict[str, bool]
