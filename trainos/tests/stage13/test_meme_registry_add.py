from trainos.kernel.evolution.memetics.meme import Meme
from trainos.kernel.evolution.memetics.meme_registry import MemeRegistry
from trainos.kernel.evolution.memetics.meme_type import MemeType


def test_meme_registry_add():

    registry = MemeRegistry()

    meme = Meme(
        type=MemeType.BELIEF,
        content="cooperation",
    )

    registry.add(meme)

    assert registry.memes() == (meme,)