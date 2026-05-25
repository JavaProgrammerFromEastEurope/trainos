import heapq

class AStar:

    @staticmethod
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @staticmethod
    def neighbors(node):
        x, y = node
        return [(x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)]

    @staticmethod
    def find_path(start, goal, walkable):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        while frontier:
            _, current = heapq.heappop(frontier)
            if current == goal:
                break
            for next_node in AStar.neighbors(current):
                if next_node not in walkable:
                    continue
                new_cost = cost_so_far[current] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + AStar.heuristic(goal, next_node)
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current
        if goal not in came_from:
            return []
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path
