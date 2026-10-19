from .weakness import Weakness


class WeaknessDetector:

    def detect(
        self,
    ) -> Weakness:
        return Weakness(name="navigation")
