from trainos.kernel.learning.episodes.episode import Episode
from trainos.kernel.learning.episodes.episode_step import EpisodeStep


def test_episode_system():

    episode = Episode()
    step = EpisodeStep(reward=1.0)

    episode.add_step(step)
    steps = episode.steps()

    assert len(steps) == 1
    assert steps[0] == step
