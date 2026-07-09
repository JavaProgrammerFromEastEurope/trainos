from kernel.population.professions.profession import Profession
from kernel.population.professions.profession_category import ProfessionCategory
from kernel.population.professions.profession_engine import ProfessionEngine
from kernel.population.professions.profession_type import ProfessionType


def test_profession_engine():

    engine = ProfessionEngine()
    profession = Profession(
        profession_id="ENG",
        name="Engineer",
        profession_type=ProfessionType.ENGINEER,
        category=ProfessionCategory.INDUSTRIAL,
    )

    assigned 	= engine.assign(profession)
    validated = engine.validate(assigned)

    assert validated is profession