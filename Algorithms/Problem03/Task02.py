# FUNCTION CODE

# IMPORTING GRAPH IN ADJACENCY LIST FROM TASK01
from Task01 import *

graph = aList

# INITIALISING VISITED ARRAY WITH ZERO, QUEUE AS AN EMPTY LIST AND TREE LIST FOR THE OUTPUT
visited = [0] * no_of_nodes
queue = []
tree = []


def BFS(visited, graph, node, endPoint):
    # CONVERTING THE NODE AND ENDPOINT INTO INTEGERS
    node = int(node)
    endPoint = int(endPoint)

    # AS THE FIRST NODE IS VISITED, ITS INDEX VALUE ON VISITED ARRAY BECOMES ZERO
    # THE NODE GETS APPENDED TO THE QUEUE
    visited[int(node) - 1] = 1
    queue.append(node)

    # LOOP TO RUN UNTIL THE QUEUE IS EMPTY
    while len(queue) != 0:
        # THE FIRST ELEMENT OF THE QUEUE IS POPPED WHICH IS ALSO ADDED TO THE OUTPUT ARRAY
        m = queue.pop(0)
        tree.append(m)

        # IF THE DESTINATION IS REACHED, THE LOOP BREAKS
        if m == endPoint:
            break

        for count in range(0, connections):
            # FOR ALL THE SUBLISTS IN THE ADJACENT LIST WHICH HAVE M IN THE FIRST INDEX => WHEN M = 2 : [2,3], [2,4] [2,5]
            if int(graph[count][0]) == m:
                # THE NEIGHBOURS ARE THE NODES THAT ARE CONNECTED TO THE M NODE => WHEN M = 2 : 3, 4, 5
                neighbour = int(graph[count][1])
                if visited[neighbour - 1] == 0:
                    # THE VISITED ARRAY BECOMES 1 WHEN ANY NODE IS VISITED, ELSE REMAINS ZERO
                    # SO IF A NODE IS ALREADY VISITED, THEN THE NODE IS NOT APPENDED TO THE QUEUE
                    visited[neighbour - 1] = 1
                    queue.append(neighbour)

    return tree


# DRIVER CODE

tree = BFS(visited, graph, "1", "12")

writer = open("output2.txt", "w")

writer.write("Places:" + " ")
for item in tree:
    writer.write(str(item) + " ")
writer.close()
