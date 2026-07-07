from enum import Enum


class ProductionCategory(Enum):

    CONTINUOUS 	= "continuous"
    BATCH 			= "batch"
    ON_DEMAND 	= "on_demand"