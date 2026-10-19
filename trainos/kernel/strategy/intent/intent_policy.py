from dataclasses import dataclass


@dataclass(frozen=True)
class IntentPolicy:

    allow_intent_override: bool
