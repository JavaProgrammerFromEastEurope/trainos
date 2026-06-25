from enum import Enum


class HypothesisStatus(Enum):

    PROPOSED 	= "proposed"
    TESTING 	= "testing"
    CONFIRMED = "confirmed"
    REJECTED 	= "rejected"