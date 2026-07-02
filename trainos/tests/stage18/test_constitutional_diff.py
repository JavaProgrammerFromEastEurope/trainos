from trainos.kernel.constitution.diff.constitutional_diff import ConstitutionalDiff
from trainos.kernel.constitution.diff.diff_result import DiffResult


def test_constitutional_diff():

    diff = ConstitutionalDiff(
        from_version="2.0",
        to_version="2.1",
        result=DiffResult.MODIFIED,
    )

    assert diff.result == DiffResult.MODIFIED