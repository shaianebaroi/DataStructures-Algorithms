# =========================== FUNCTION CODE ==============================
import heapq


def Network(graph, source):

    # SLICING THE GRAPH INTO ITS LIMITS AND ADJACENT LIST
    limit = int(graph[0][0]) + 1
    graph.pop(0)
    # print(graph)
    # print(limit)

    # INITIALISATION OF THE ARRAYS
    dist = [float("-inf")] * limit
    prev = [0] * limit
    # visited = [0] * limit
    pq = []
    a = []
    neighbour = 1

    dist[source] = float("inf")

    for count in range(0, len(graph)):

        v = int(graph[count][0])
        if v != source:
            dist[v] = float("-inf")
            prev[v] = None
        heapq.heappush(pq, [dist[v], v])
        # visited[v] = False

    while len(pq) != 0:
        a = heapq.heappop(pq)
        u = a[1]
        # if visited[u] == True:
        # continue
        # visited[u] = True

        for count in range(0, len(graph)):
            if int(graph[count][0]) == u:
                neighbour = int(graph[count][1])
                length = int(graph[count][2])
                alt = min(dist[u], length)
                if alt > dist[neighbour]:
                    dist[neighbour] = alt
                    prev[neighbour] = u
                    heapq.heappush(pq, [dist[neighbour], neighbour])

    # return (dist, prev)
    return dist


# =========================== DRIVER CODE ==============================

reader = open("input4.txt", "r")
writer = open("output4.txt", "w")

# TAKING THE NUMBER OF TEST CASES
n = reader.readline()
testcases = int(n)
# print("Testcases: " + str(testcases))

# INPUTTING VALUES FROM EACH LINE IN A LIST AS STRING
for count in range(0, testcases):
    # print("Testcase " + str(count) + ":")
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

    source = reader.readline()
    source = int(source)
    # print("Source : ", source)

    graph = aList + bList
    # print(graph)
    longest_path = Network(graph, source)

    # PRINTNG
    longest_path.pop(0)
    for count in range(0, len(longest_path)):
        if longest_path[count] == float("inf"):
            longest_path[count] = 0
        elif longest_path[count] == float("-inf"):
            longest_path[count] = -1
    for count in range(0, len(longest_path)):
        writer.write(str(longest_path[count]) + " ")
    writer.write("\n")
