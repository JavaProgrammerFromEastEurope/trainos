from trainos.kernel.constitution.justification.constitutional_justification import (
    ConstitutionalJustification,
)
from trainos.kernel.constitution.justification.justification_type import (
    JustificationType,
)


def test_constitution_justification():

    justification = ConstitutionalJustification(
        proposal="Emergency law",
        type=JustificationType.ARTICLE_REFERENCE,
        explanation="Protected by Article 5",
    )

    assert justification.type == JustificationType.ARTICLE_REFERENCE
