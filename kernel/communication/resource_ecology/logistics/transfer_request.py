from dataclasses import dataclass


@dataclass
class TransferRequest:

    resource: str
    amount: 	float
    source: 	str
    target: 	str