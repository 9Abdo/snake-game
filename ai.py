import heapq
import config

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, snake_body):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        neighbors = [
            (current[0]+1, current[1]),
            (current[0]-1, current[1]),
            (current[0], current[1]+1),
            (current[0], current[1]-1)
        ]

        for n in neighbors:
            if 0 <= n[0] < config.GRID_SIZE and 0 <= n[1] < config.GRID_SIZE and n not in snake_body:
                temp_g = g_score[current] + 1

                if n not in g_score or temp_g < g_score[n]:
                    came_from[n] = current
                    g_score[n] = temp_g
                    f = temp_g + heuristic(n, goal)
                    heapq.heappush(open_set, (f, n))

    return []