# =========================== FUNCTION CODE ==============================
import heapq


def Dijkstra(graph, source):

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
            if int(graph[count][0]) == u:  # SEARCHING FOR THE VERTEX WHICH WAS POPPED
                neighbour = int(graph[count][1])
                length = int(graph[count][2])
                alt = dist[u] + length
                if alt < dist[neighbour]:
                    dist[neighbour] = alt
                    prev[neighbour] = u
                    heapq.heappush(pq, [dist[neighbour], neighbour])

    # return (dist, prev)

    last = len(dist) - 1
    return dist[last]


# =========================== DRIVER CODE ==============================

reader = open("input1.txt", "r")
writer = open("output1.txt", "w")


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
    shortest_path = Dijkstra(graph, 1)
    writer.write(str(shortest_path) + "\n")

reader.close()
writer.close()
