from kernel.education.definitions.education_category import EducationCategory
from kernel.education.definitions.education_definition import EducationDefinition
from kernel.education.definitions.education_type import EducationType


def test_education_definition():

    definition = EducationDefinition(
        education_id="engineering",
        name="Engineering",
        education_type=EducationType.TECHNICAL,
        category=EducationCategory.PROFESSIONAL,
    )

    assert definition.education_id == "engineering"
    assert definition.name == "Engineering"
    assert definition.education_type == EducationType.TECHNICAL
    assert definition.category == EducationCategory.PROFESSIONAL