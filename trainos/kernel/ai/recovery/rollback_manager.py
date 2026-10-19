from __future__ import annotations


class RollbackManager:

    def rollback(
        self,
        completed_nodes: list[str],
    ) -> list[str]:
        result = []
        for node in reversed(completed_nodes):
            result.append(node)
        return result
