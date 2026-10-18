import pytest
from kernel.command.execution.execution_progress import ExecutionProgress


def test_progress_rejects_invalid_counters_and_non_boolean_completion():
    assert ExecutionProgress(0, 1, False).completed is False
    assert ExecutionProgress(3, 3, True).attempts == 3
    for args in [(-1, 3, False), (0, 0, False), (4, 3, True)]:
        with pytest.raises(ValueError):
            ExecutionProgress(*args)
    with pytest.raises(TypeError):
        ExecutionProgress(0, 1, 1)
