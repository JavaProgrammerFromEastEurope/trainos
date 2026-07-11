from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SkillPolicy:

    allow_upgrade: bool = True