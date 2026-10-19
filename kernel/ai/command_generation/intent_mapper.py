from __future__ import annotations


class IntentMapper:

    def map(self, intent: str) -> str:
        if intent == "recover":
            return "trigger_recovery"
        if intent == "init":
            return "initialize_state"
        return "noop"
