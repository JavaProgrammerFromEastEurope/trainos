class ExecutionPlanner:

    def __init__(self, compiler, allocator):
        self.compiler 	= compiler
        self.allocator 	= allocator

    def build_execution_plan(self, goal, entity_pool):
        tasks = self.compiler.compile(goal)
        execution_plan = []
        for task in tasks:
            assigned = self.allocator.allocate(
                task,
                entity_pool,
            )
            execution_plan.append(
                {
                    "task": task,
                    "entities": assigned,
                }
            )
        return execution_plan

