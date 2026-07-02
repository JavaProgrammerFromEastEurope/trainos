from trainos.kernel.constitution.amendment.integration.constitutional_integration import ConstitutionalIntegration
from trainos.kernel.constitution.amendment.integration.integration_result import IntegrationResult


def test_constitutional_integration():

    integration = ConstitutionalIntegration(
        proposal_id="A-001",
        new_version="2.1",
        result=IntegrationResult.SUCCESS,
    )

    assert integration.new_version == "2.1"