from dataclasses import dataclass


@dataclass(frozen=True)
class PricingRule:

    rule_id: 			str
    description: 	str