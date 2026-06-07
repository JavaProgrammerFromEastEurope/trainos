from dataclasses import dataclass


@dataclass
class GoalScore:

    goal_id: str
    utility: float
    risk: float
    final_score: float


class UtilityScorer:

    def score(self, goal, memory, snapshot):
        base = goal.priority
        risk = self._risk(goal, snapshot)
        context_bonus = self._context(goal, memory)
        final = base + context_bonus - risk
        return GoalScore(
            goal_id=goal.goal_id,
            utility=base,
            risk=risk,
            final_score=final,
        )

    def _risk(self, goal, snapshot):
        if goal.__class__.__name__ == "EvacuateSectorGoal":
            return 50  # дорого и опасно
        if goal.__class__.__name__ == "ContainLeakGoal":
            return 10  # локально безопасно
        return 20

    def _context(self, goal, memory):
        sector = memory.get(goal.sector_id)
        return sector.instability_score * 30
