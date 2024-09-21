import numpy as np
def find_shortest_path(city, path, total_distance):
    global shortest_path
    global min_distance
    if len(path) == number_of_cities:
        total_distance += distance[city][0]
        if total_distance < min_distance:
            min_distance = total_distance
            shortest_path = path + [0]
        return
    for k in range(number_of_cities):
        if k not in path and distance[city][k] != 0:
            find_shortest_path(k, path + [k], total_distance + distance[city][k])
distance = np.array([[0,10,15,20],
                     [10,0,35,25],
                     [15,35,0,30],
                     [20,25,30,0]])
number_of_cities = 4
min_distance = float('inf')
shortest_path = []
find_shortest_path(0, [0], 0)
print("Shortest Path:", end=" ")
for city in shortest_path:
    print(city + 1, end=" ")
print()
print("Minimum Distance:", end=" ")
print(min_distance)