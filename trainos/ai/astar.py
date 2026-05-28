import heapq


def heuristic(a, b):
    #
    # Manhattan distance
    #
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node):
    x, y = node
    #
    # 4-direction movement
    #
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def is_walkable(sector, x, y, occupancy_map=None, ignore_entity=None):
    #
    # WORLD BOUNDS
    #
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= sector.width:
        return False
    if y >= sector.height:
        return False
    #
    # CELL LOOKUP
    #
    cell = sector.get_cell(x, y)
    if not cell:
        return False
    #
    # STATIC WALLS
    #
    if not cell.walkable:
        return False
    #
    # DYNAMIC OCCUPANCY
    #
    if occupancy_map:
        occupied_entity = occupancy_map.get_entity(x, y)
        if occupied_entity is not None:
            if occupied_entity != ignore_entity:
                return False
    return True


def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path


def astar(sector, start, goal, occupancy_map=None, ignore_entity=None):
    #
    # INVALID GOAL
    #
    if not is_walkable(sector, goal[0], goal[1], occupancy_map, ignore_entity):
        return []
    #
    # FRONTIER
    #
    frontier = []
    heapq.heappush(frontier, (0, start))
    #
    # SEARCH TABLES
    #
    came_from = {start: None}
    cost_so_far = {start: 0}
    #
    # MAIN LOOP
    #
    while frontier:
        _, current = heapq.heappop(frontier)
        #
        # GOAL REACHED
        #
        if current == goal:
            break
        #
        # EXPAND NEIGHBORS
        #
        for neighbor in get_neighbors(current):
            nx, ny = neighbor
            #
            # BLOCKED CELL
            #
            if not is_walkable(sector, nx, ny, occupancy_map, ignore_entity):
                continue
            #
            # MOVEMENT COST
            #
            new_cost = cost_so_far[current] + 1
            #
            # BETTER PATH
            #
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    #
    # PATH NOT FOUND
    #
    if goal not in came_from:
        return []
    #
    # BUILD PATH
    #
    return reconstruct_path(came_from, goal)
