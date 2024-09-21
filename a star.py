import heapq

def a_star(graph, start, goal, heuristic):
    open_set = [(start, 0)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        open_set.sort(key=lambda x: f_score[x[0]])
        current = open_set.pop(0)[0]

        if current == goal:
            path = []
            total_cost = g_score[goal]
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], total_cost

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in [i[0] for i in open_set]:
                    open_set.append((neighbor, f_score[neighbor]))

    return None, float('inf')

def heuristic(node, goal):
    # Define your heuristic here
    h_dist = {
        'S': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11,'G':0
    }
    return h_dist[node]

def main():
    # Example graph
    graph = {
        'S': [('B', 4), ('C', 3)],
        'B': [('S', 4), ('F', 5), ('E', 12)],
        'C': [('E', 10), ('D', 7),('S',3)],
        'D': [('C', 7),('E',2)],
        'E': [('B', 12), ('G', 5),('C',10)],
        'F': [('B', 5), ('G', 16)],
        'G':[('E',5),('F',16)]
    }

    # Take user input for start and goal nodes
    start_node = input("Enter the start node: ").strip().upper()
    goal_node = input("Enter the goal node: ").strip().upper()

    # Run A* search
    path, distance = a_star(graph, start_node, goal_node, heuristic)

    if path:
        print("Shortest path from {} to {}: {}".format(start_node, goal_node, path))
        print("Path distance: {}".format(distance))
    else:
        print("No path found from {} to {}.".format(start_node, goal_node))

if __name__ == "__main__":
    main()
