from dataclasses import dataclass

from .hypothesis_status import HypothesisStatus


@dataclass
class Hypothesis:

    description: str
    status: HypothesisStatus