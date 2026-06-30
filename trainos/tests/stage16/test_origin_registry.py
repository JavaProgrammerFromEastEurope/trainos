from trainos.kernel.identity.principles.origin.origin_registry import OriginRegistry
from trainos.kernel.identity.principles.origin.principle_origin import PrincipleOrigin
from trainos.kernel.identity.principles.origin.origin_type import OriginType


def test_origin_registry():
    registry = OriginRegistry()

    origin = PrincipleOrigin(
        description="Founder doctrine",
        type=OriginType.FOUNDER
    )

    registry.register(origin)

    assert len(registry.origins()) == 1