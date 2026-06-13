from trainos.kernel.ai.decision.decision import Decision
from trainos.kernel.ai.command_generation.command_generator import CommandGenerator


def test_command_generation():

    generator = CommandGenerator()
    decisions = [Decision(action="initialize_state", confidence=1.0, payload={})]
    commands 	= generator.generate(decisions)
    assert len(commands) == 1
