class TaskScorer:

    @staticmethod
    def score_task(spatial, task):
        dx = abs(spatial.cell_x - task.target_x)
        dy = abs(spatial.cell_y - task.target_y)
        distance = dx + dy
        priority_score = task.priority * 100
        distance_penalty = distance * 5
        final_score = priority_score - distance_penalty
        return final_score
