# FUNCTION CODE

# IMPORTING GRAPH IN ADJACENCY LIST FROM TASK01
from Task01 import *

writer = open("output3.txt", "w")

# INITIALISING VISITED ARRAY WITH ZERO, QUEUE AS AN EMPTY LIST AND TREE LIST FOR THE OUTPUT
visited = [0] * no_of_nodes
printed = []
graph = aList


# RECURSION FOLLOWS THE PRINCIPLES OF STACK
def DFS_VISIT(graph, node):
    visited[int(node) - 1] = 1
    printed.append(node)

    for count in range(0, connections):
        # CHECKS IF THE LAST NODE IS EQUAL TO THE FIRST NODE OF ANOTHER CONNECTION => WHEN NODE = 3 : [2,3], [3,4]
        # IN CASE IF THIS CONDITION DOES NOT FULFILL => WHEN NODE = 4 : [3, 4], NO CONNECTION HAS 4 AS ITS FIRST NODE
        # THE CONDITION REVERTS BACK TO ITS PREVIOUS NODE (POPS, STACK): NEW NODE = 3, SO OTHER NODES ARE EXPLORED
        if node == int(graph[count][0]):
            # IF THE NODES ARE EQUAL, THEN THE NEIGHBOUR OF THE LAST NODE BECOMES THE NEW NODE => NEW NODE = 4
            index = int(graph[count][1])
            if visited[index - 1] == 0:
                DFS_VISIT(graph, index)


def DFS(graph, endPoint):

    for count in range(0, connections):
        node = int(graph[count][0])
        # THIS CONDITION ENSURES THAT ONLY NODES WHICH HAVE ALREADY BEEN VISITED ARE AVOIDED
        if visited[node - 1] == 0:
            DFS_VISIT(graph, node)

    # print(printed)
    writer.write("Places: ")
    for item in printed:
        writer.write(str(item) + " ")
        # ENDPOINT CONDITION
        if item == int(endPoint):
            break


# DRIVE CODE
DFS(graph, "12")
writer.close()
