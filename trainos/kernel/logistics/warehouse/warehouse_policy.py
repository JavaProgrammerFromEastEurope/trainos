from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WarehousePolicy:

    allow_storage: bool 	= True
    allow_dispatch: bool 	= True