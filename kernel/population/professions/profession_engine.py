from .profession import Profession


class ProfessionEngine:

    def assign(
        self,
        profession: Profession,
    ) -> Profession:
        return profession

    def validate(
        self,
        profession: Profession,
    ) -> Profession:
        return profession