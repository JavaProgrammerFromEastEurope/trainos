from dataclasses import dataclass


@dataclass(frozen=True)
class CurrencyDefinition:

    currency_id: 			str
    code: 						str
    name: 						str
    symbol: 					str
    fractional_digits: int