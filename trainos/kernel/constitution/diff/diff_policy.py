from dataclasses import dataclass


@dataclass(frozen=True)
class DiffPolicy:

    compare_structure: bool
    compare_content:	 bool