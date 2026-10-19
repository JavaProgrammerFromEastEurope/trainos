from dataclasses import dataclass

from .simulation_audit_type import SimulationAuditType


@dataclass(frozen=True, slots=True)
class SimulationAuditEntry:

    audit_id: 	str
    tick: 			int
    audit_type: SimulationAuditType
    message: 		str