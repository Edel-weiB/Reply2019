# DONT USE THIS !!!!
import math
import random


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
    
    for y in range(map_size_y):
        for x in range(map_size_x):
            print(map_terrain[y][x],end='')
        print()


def read_file(filename):
    fp = open(filename, 'r')
    read_maps(fp, 50, 50)
    fp.close()

def cluster(cluster_needed, office_map):
    # Initialise variable
    max_cluster = len(office_map)
    min_distance = 0 
    min_i_cluster = 0
    min_j_cluster = 0

    # Initialise 2d array
    cluster_data = [[[] for column in range(max_cluster)] for row in range(max_cluster)]
    cluster_title = [[] for item in range(max_cluster)]

    # Populate 2d array
    for j in range(max_cluster):
        cluster_title[j] = [office_map[j]]
        for i in range(max_cluster):
            if i >= j:
                if i == j:
                    cluster_data[j][i] = [0]
                else:
                    cluster_data[j][i] = [dijkstra_distance(
                        [office_map[j][0], office_map[j][1]],
                        [office_map[i][0], office_map[i][1]]
                        )]
            else:
                cluster_data[j][i] = cluster_data[i][j]

    # print function
    def print_cluster():
        print("Title: ",end='')
        for title in range(len(cluster_title)):
            print(cluster_title[title],end='')
        print()
        for j in range(max_cluster):
            for i in range(max_cluster):
                print(cluster_data[j][i], end='')
            print()

    print_cluster()

    while max_cluster > cluster_needed:
        # min distance
        min_distance = math.inf
        min_i_cluster = 0
        min_j_cluster = 0
        for j in range(max_cluster):
            for i in range(j, max_cluster):
                for entry in cluster_data[j][i]:
                    if entry != 0:
                        if entry < min_distance:
                            min_distance = entry
                            min_i_cluster = i
                            min_j_cluster = j

        print(min_i_cluster)
        print(min_j_cluster)

        # Combine 2d array
        if min_i_cluster > min_j_cluster:
            max_cluster = min_i_cluster
            min_cluster = min_j_cluster
        else:
            max_cluster = min_j_cluster
            min_cluster = min_i_cluster
        for i in range(max_cluster):
            for item in cluster_data[i][min_cluster]:
                cluster_data[i][max_cluster].append(item)

        # Combine the title
        for item in cluster_title[min_i_cluster]:
            cluster_title[min_j_cluster].append(item)
        # Remove unneeded column and row
        max_cluster = max_cluster - 1
        #new_cluster_data = [[[] for column in range(max_cluster)] for row in range(max_cluster)]
        #temp_j = 0
        #j = 0
        #while j < max_cluster:
        #    if j == min_i_cluster:
        #        temp_j = temp_j + 1
        #    temp_i = 0
        #    i = 0
        #    while i < max_cluster:
        #        if i == min_i_cluster:
        #            temp_i = temp_i + 1
        #        new_cluster_data[j][i] = cluster_data[temp_j][temp_i]
        #        temp_i = temp_i + 1
        #        i = i + 1
        #    temp_j = temp_j + 1
        #    j = j + 1
        ## Update cluster
        #cluster_data = None
        #cluster_data = new_cluster_data
        #new_cluster_data = None

        print_cluster()

def main():
    print("buffer")
    cluster(3, [
        [15, 1, 1700],
        [14, 6, 1200],
        [3, 8, 1100],
        #[17, 9, 1050],
        #[8, 10, 700],
        [13, 6, 900]
        ])

def dijkstra_distance(a, b):
    return random.randint(1, 9)

main()