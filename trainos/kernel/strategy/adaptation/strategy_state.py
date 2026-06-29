from enum import Enum


class StrategyState(Enum):

    STABLE 			= "stable"
    ADAPTING 		= "adapting"
    RECOVERING 	= "recovering"