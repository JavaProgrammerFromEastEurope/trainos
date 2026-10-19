from kernel.security.officers.security_officer_policy import SecurityOfficerPolicy
from kernel.security.incidents.security_incident_policy 	import SecurityIncidentPolicy
from kernel.security.patrols.security_patrol_policy 			import SecurityPatrolPolicy
from kernel.security.facilities.security_facility_policy 	import SecurityFacilityPolicy


def test_security_policies():

    officer_policy 	= SecurityOfficerPolicy()
    incident_policy = SecurityIncidentPolicy()
    patrol_policy 	= SecurityPatrolPolicy()
    facility_policy = SecurityFacilityPolicy()

    assert officer_policy.allow_dispatch is True
    assert incident_policy.allow_resolution is True
    assert patrol_policy.allow_activation is True
    assert facility_policy.allow_operation is True
