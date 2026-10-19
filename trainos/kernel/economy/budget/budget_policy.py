from dataclasses import dataclass


@dataclass(frozen=True)
class BudgetPolicy:

    immutable_budget: 		bool
    allow_negative_plan: 	bool