from dataclasses import dataclass


@dataclass(frozen=True)
class TreasuryFund:

    fund_id: 			str
    treasury_id: 	str
    name: 				str