from .reasoning_result 	import ReasoningResult
from .reasoning_task 		import ReasoningTask


class ReasoningEngine:

    def reason(self, task: ReasoningTask) -> ReasoningResult:
        return ReasoningResult(conclusion=task.description)
