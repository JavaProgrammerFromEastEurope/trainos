from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class RecipeInput:

    resource_id: str
    quantity: Decimal