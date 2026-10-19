from dataclasses import dataclass

from .integration_result import IntegrationResult


@dataclass(frozen=True)
class ConstitutionalIntegration:

    proposal_id: str
    new_version: str
    result: IntegrationResult