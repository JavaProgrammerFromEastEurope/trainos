class SafetyConstraints:

    def validate(self, goals, snapshot):
        valid = []
        for g in goals:
            if self._violates(g, snapshot):
                continue
            valid.append(g)
        return valid

    def _violates(self, goal, snapshot):
        if goal.__class__.__name__ == "EvacuateSectorGoal":
            sector = snapshot.sectors.get(goal.source_sector)
            if sector.oxygen > 85:
                return True  # нет необходимости
        return False
