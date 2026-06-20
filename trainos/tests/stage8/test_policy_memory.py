from trainos.kernel.learning.policy_memory.policy_history import PolicyHistory
from trainos.kernel.learning.policy_memory.policy_version import PolicyVersion


def test_policy_memory():

    history = PolicyHistory()
    version = PolicyVersion(version=1)

    history.add(version)
    versions = history.versions()

    assert len(versions) == 1
    assert versions[0] == version
