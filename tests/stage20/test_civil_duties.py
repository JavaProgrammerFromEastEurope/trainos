from kernel.society.duties.civil_duty import CivilDuty
from kernel.society.duties.civil_duty_set import CivilDutySet


def test_create_duty_set():

    duties = CivilDutySet(
        entity_id="A-104",
        duties=(
            CivilDuty.OBEY_CONSTITUTION,
            CivilDuty.PAY_TAXES,
        ),
    )

    assert len(duties.duties) == 2
    assert CivilDuty.PAY_TAXES in duties.duties
