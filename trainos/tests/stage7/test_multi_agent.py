from trainos.kernel.behavior.multi_agent.agent_group import (
    AgentGroup,
)

from trainos.kernel.behavior.multi_agent.agent_member import (
    AgentMember,
)

from trainos.kernel.behavior.multi_agent.agent_role import (
    AgentRole,
)


def test_multi_agent():

    group 	= AgentGroup()
    member 	= AgentMember(id="drone1", role=AgentRole.LEADER)

    group.add(member)
    members = group.members()

    assert len(members) == 1
    assert members[0] is member
    assert members[0].role == AgentRole.LEADER
