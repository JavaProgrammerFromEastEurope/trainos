from dataclasses import dataclass


@dataclass
class NegotiationOffer:

    sender: str
    receiver: str
    proposal: str