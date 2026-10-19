from dataclasses import dataclass


@dataclass(frozen=True)
class Valuation:

    valuation_id: str
    subject_id: 	str
    rule_id: 			str