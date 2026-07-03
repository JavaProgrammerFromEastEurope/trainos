from dataclasses import dataclass


@dataclass(frozen=True)
class Budget:

    budget_id: 		str
    treasury_id: 	str
    fiscal_year: 	int