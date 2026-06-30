from trainos.kernel.identity.principles.origin.principle_origin import PrincipleOrigin
from trainos.kernel.identity.principles.origin.origin_type import OriginType


def test_principle_origin():
    origin = PrincipleOrigin(
        description="Created after system failure",
        type=OriginType.HISTORICAL_EVENT
    )

    assert origin.type == OriginType.HISTORICAL_EVENT