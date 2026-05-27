from dataclasses import dataclass


@dataclass(slots=True)
class Task:

    task_id: str
    task_type: str
    target_wagon: str
    target_sector: str
    target_x: int
    target_y: int
    priority: int = 1
    assigned_entity: int | None = None
    completed: bool = False
