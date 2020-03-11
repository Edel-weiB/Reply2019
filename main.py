import math

# Terrain
M = math.inf # Mountain
W = 800 # Water
T = 200 # Traffic jam
D = 150 # Dirt
R = 120 # RAILWAY_LEVEL_CROSSING
S = 100 # STANDARD_TERRIAN
H = 70 # HIGHWAY
R = 50 # RAILWAY

POSITION = ['N', 'S', 'E', 'W']


def read_coordinates(fptr):
    # no_of_offices: [GridWidth, GridHeight, Customer Offices, Reward Offices]
    # office_map: [X_Position, Y_position, Reward of Customer HQ]
    grid_layout=fptr.readline().split(' ')
    #Integer Typecasting
    grid_layout[0]= int(grid_layout[0])
    grid_layout[1]= int(grid_layout[1])
    grid_layout[2]= int(grid_layout[2])
    grid_layout[3]= int(grid_layout[3])
    no_of_offices = int(grid_layout[2])
    office_map = {}
    for i in range(no_of_offices):
        office_map[i]=fptr.readline().split(' ')
    return (grid_layout, office_map)



def read_maps(fptr, map_size_x, map_size_y):
    map_terrain = [[0 for column in range(map_size_x)] for row in range(map_size_y)]
    # map_terrain = [([0]*map_size_y) for i in range(map_size_x)]

    for y in range(map_size_y):
        grid_layout = fptr.readline()
        for x in range(map_size_x):
            # Check for mountain
            if grid_layout[x] == "#":
                map_terrain[y][x] = math.inf
            # Check for water
            elif grid_layout[x] == "~":
                map_terrain[y][x] = 800
            # Check for Traffic jam
            elif grid_layout[x] == "*":
                map_terrain[y][x] = 200
            # Check for Dirt
            elif grid_layout[x] == "+":
                map_terrain[y][x] = 150
            # Check for Railway level crossing
            elif grid_layout[x] == "X":
                map_terrain[y][x] = 120
            # Check for Standard terrain
            elif grid_layout[x] == "_":
                map_terrain[y][x] = 100
            # Check for Highway
            elif grid_layout[x] == "H":
                map_terrain[y][x] = 70
            # Check for Railway (Every thing else)
            else:
                map_terrain[y][x] = 50

    return map_terrain
    
    # for y in range(map_size_y):
    #     for x in range(map_size_x):
    #         print(map_terrain[y][x],end='')
    #     print()


def find_next_neighbour(map_visited, x, y):
    #  right, down, left, up
    nearest_neighbour_coords = [(x+1, y), (x,y-1), (x-1,y),(x,y+1)]
    for coords in nearest_neighbour_coords:
        if(map_visited[coords[0]][coords[1]] or coords[0]<0 or coords[1]<0 or coords[0]>len(map_visited) or coords[1]>len(map_visited)):
            nearest_neighbour_coords.remove(coords)
    return nearest_neighbour_coords
    
# function Dijkstra(Graph, source):
# 3
# 4      create vertex priority queue Q
# 5
# 6      for each vertex v in Graph:           
# 7          if v ≠ source
# 8              dist[v] ← INFINITY                 // Unknown distance from source to v
# 9              prev[v] ← UNDEFINED                // Predecessor of v
# 10
# 11         Q.add_with_priority(v, dist[v])
# 12
# 13
# 14     while Q is not empty:                      // The main loop
# 15         u ← Q.extract_min()                    // Remove and return best vertex
# 16         for each neighbor v of u:              // only v that are still in Q
# 17             alt ← dist[u] + length(u, v) 
# 18             if alt < dist[v]
# 19                 dist[v] ← alt
# 20                 prev[v] ← u
# 21                 Q.decrease_priority(v, alt)
# 22
# 23     return dist, prev


def dijkstra_distance(map_terrain,map_size):
    
    
    point1x = 2
    point1y = 5
    current_point = (point1x, point1y)
    point2x = 10
    point2y = 20
    # True for mountain areas
    # False for all other terrians
    map_visited = [[True if map_terrain[row][column] == math.inf else False for column in range(map_size[0])] for row in range(map_size[1])]
    
    # Distance list
    dist_list = [[math.inf for column in range(map_size[0])] for row in range(map_size[1])]
    dist_list[point1x][point1y] = 0

    # Previous list
    prev_list = [[0 for column in range(map_size[0])] for row in range(map_size[1])]
    prev_list[point1x][point1y] = -1
    
    #Dijkstra.?
    while True:
        queue = find_next_neighbour(map_visited, current_point[0],current_point[1])
        print(queue)
        if len(queue) == 0:
            break
        for point in queue:
            # yet to visit = false
            if not map_visited[point[0]][point[1]]:
                # edge/weight
                pt_edge = map_terrain[point[0]][point[1]]
                # print(map_terrain[point[0]][point[1]])
                # print(pt_edge)
                cur_dist = dist_list[current_point[0]][current_point[1]]
                pt_dist = dist_list[point[0]][point[1]]
                
                if cur_dist + pt_edge < pt_dist:
                    dist_list[point[0]][point[1]] = cur_dist + pt_edge
                    prev_list[point[0]][point[1]] = (current_point[0], current_point[1])

        map_visited[current_point[0]][current_point[1]] = True
        current_point = (point[0], point[1])

    
    print(dist_list)
            

def read_file(filename):
    fp = open(filename, 'r')
    (grid_layout, office_map)=read_coordinates(fp)
    print(type(grid_layout[0]), type(grid_layout[1]))
    map_terrain = read_maps(fp, grid_layout[0], grid_layout[1])
    fp.close()
    return (map_terrain,grid_layout)

def main():
    (map_terrian, grid_layout) = read_file("1_victoria_lake.txt")
    dijkstra_distance(map_terrian, grid_layout)




if __name__ == "__main__":
    main()