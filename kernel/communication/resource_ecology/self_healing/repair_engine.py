from .repair_plan import RepairPlan


class RepairEngine:

    def repair(self) -> RepairPlan:
        return RepairPlan(
            description="replace damaged hydroponics module",
        )
