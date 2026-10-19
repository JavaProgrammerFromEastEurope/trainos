from .drift_measurement import DriftMeasurement


class IdentityDriftEngine:

    def measure(self) -> DriftMeasurement:
        return DriftMeasurement(value=0.0)
