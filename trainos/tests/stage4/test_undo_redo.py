from trainos.kernel.command_bus.command_stack import CommandStack
from trainos.kernel.command_bus.undoable_command import UndoableCommand


class Fake(UndoableCommand):

    def __init__(self):
        self.undone = False

    def undo(self):
        self.undone = True


def test_undo_redo():

    stack = CommandStack()
    cmd = Fake()
    stack.push(cmd)

    stack.undo()
    assert cmd.undone is True

    stack.redo()
    assert len(stack._executed) == 1
