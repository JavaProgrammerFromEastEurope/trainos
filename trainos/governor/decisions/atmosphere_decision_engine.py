class AtmosphereDecisionEngine:

    def __init__(
        self,
        scorer,
        resolver,
        safety,
    ):
        self.scorer = scorer
        self.resolver = resolver
        self.safety = safety

    def decide(self, goals, memory, snapshot):
        scored = []
        for g in goals:
            score = self.scorer.score(
                g,
                memory,
                snapshot,
            )
            scored.append((g, score))
        scored.sort(
            key=lambda x: x[1].final_score,
            reverse=True,
        )
        filtered = self.safety.validate(
            [g for g, _ in scored],
            snapshot,
        )
        resolved = self.resolver.resolve([s for s in scored if s[0] in filtered])
        return resolved
