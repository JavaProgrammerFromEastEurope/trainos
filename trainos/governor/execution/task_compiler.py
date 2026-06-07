class TaskCompiler:

    def compile(self, goal):
        if goal.__class__.__name__ == "ContainLeakGoal":
            return [
                {
                    "type": "MOVE",
                    "target_sector": goal.sector_id,
                },
                {
                    "type": "CONTAIN",
                    "sector_id": goal.sector_id,
                },
            ]
        if goal.__class__.__name__ == "IncreaseOxygenGoal":
            return [
                {
                    "type": "MOVE",
                    "target_sector": goal.sector_id,
                },
                {
                    "type": "ACTIVATE_OXYGEN",
                    "sector_id": goal.sector_id,
                    "amount": goal.deficit,
                },
            ]
        if goal.__class__.__name__ == "EvacuateSectorGoal":
            return [
                {
                    "type": "MOVE_POPULATION",
                    "from": goal.source_sector,
                    "to": goal.target_sectors,
                }
            ]
