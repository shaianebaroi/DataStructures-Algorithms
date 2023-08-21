# =========================== FUNCTION CODE ==============================
import heapq


def Dijkstra_modified(graph, source):

    # SLICING THE GRAPH INTO ITS LIMITS AND ADJACENT LIST
    limit = int(graph[0][0]) + 1
    graph.pop(0)
    # print(graph)
    # print(limit)

    # INITIALISATION OF THE ARRAYS
    dist = [float("inf")] * limit
    prev = [0] * limit
    visited = [0] * limit
    pq = []
    a = []
    neighbour = 1

    dist[source] = 0

    for count in range(0, len(graph)):
        v = int(graph[count][0])
        if v != source:
            dist[v] = float("inf")
            prev[v] = None
        heapq.heappush(pq, [dist[v], v])
        visited[v] = False

    while len(pq) != 0:
        a = heapq.heappop(pq)
        u = a[1]
        if visited[u] == True:
            continue
        visited[u] = True

        for count in range(0, len(graph)):
            if int(graph[count][0]) == u:
                neighbour = int(graph[count][1])
                length = int(graph[count][2])
                alt = dist[u] + length
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    prev[neighbour] = u
                    heapq.heappush(pq, [dist[neighbour], neighbour])

    # return (dist, prev)

    # PRINTNG THE PATHWAY
    pathway = []
    pathway.append(neighbour)
    count = neighbour
    while prev[count] != 0:
        val = prev[count]
        count = val
        pathway.append(val)
    return pathway


# =========================== DRIVER CODE ==============================

reader = open("input1.txt", "r")
writer = open("output2.txt", "w")

# TAKING THE NUMBER OF TEST CASES
n = reader.readline()
testcases = int(n)

# INPUTTING VALUES FROM EACH LINE IN A LIST AS STRING
for count in range(0, testcases):
    aList = []
    l = reader.readline()
    val1 = list(map(str, l.split()))
    aList.append(val1)
    # print(aList)

    limit = int(aList[0][1])
    bList = []
    for count2 in range(0, limit):
        l = reader.readline()
        val2 = list(map(str, l.split()))
        bList.append(val2)
    # print(bList)

    graph = aList + bList
    # print(graph)
    pathway = Dijkstra_modified(graph, 1)
    # print(pathway)

    # PRINTING
    count = len(pathway) - 1
    while count >= 0:
        writer.write(str(pathway[count]) + " ")
        count -= 1
    writer.write("\n")
