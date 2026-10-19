from enum import Enum


class PatientStatus(Enum):

    HEALTHY 					= "healthy"
    UNDER_OBSERVATION = "under_observation"
    IN_TREATMENT 			= "in_treatment"
    RECOVERED 				= "recovered"
    DECEASED 					= "deceased"