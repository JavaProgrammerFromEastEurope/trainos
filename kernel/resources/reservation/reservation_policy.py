from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ReservationPolicy:

    allow_overbooking: 	bool
    auto_expire: 				bool