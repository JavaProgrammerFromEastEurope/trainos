class ConflictResolver:

    def resolve(self, scored_goals):
        by_sector = {}
        for g in scored_goals:
            key = getattr(g, "sector_id", None)
            if key not in by_sector:
                by_sector[key] = []
            by_sector[key].append(g)
        resolved = []
        for sector, goals in by_sector.items():
            goals.sort(
                key=lambda g: g.final_score,
                reverse=True,
            )
            resolved.append(goals[0])
        return resolved
