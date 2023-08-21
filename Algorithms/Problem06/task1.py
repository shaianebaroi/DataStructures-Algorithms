# ====================================== FUNCTION CODE ===========================================
def LCS(x, y):
    m = len(x) + 1  # ROW
    n = len(y) + 1  # COLUMN

    c = [[0] * (n) for i in range(m)]
    t = [[None] * (n) for i in range(m)]

    for i in range(1, m):
        c[i][0] = 0
        t[i][0] = None

    for j in range(1, n):
        c[0][j] = 0
        t[0][j] = None

    for i in range(1, m):
        for j in range(1, n):

            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                t[i][j] = "diagonal"

            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                t[i][j] = "up"

            else:
                c[i][j] = c[i][j - 1]
                t[i][j] = "left"

    return (c, t)


def LCS_print(t):
    position = t[len(t) - 1][len(t) - 1]
    i = len(t) - 1
    j = len(t) - 1
    index = []

    while position != None:
        if position == "diagonal":
            index.append(i)
            position = t[i - 1][j - 1]
            i -= 1
            j -= 1
        elif position == "left":
            position = t[i][j - 1]
            j -= 1
        elif position == "up":
            position = t[i - 1][j]
            i -= 1

    return index


# ====================================== DRIVER CODE ===========================================

reader = open("input1.txt", "r")
writer = open("output1.txt", "w")
no_of_zones = reader.readline()
n = int(no_of_zones)
x = reader.readline().rstrip()
y = reader.readline().rstrip()

y_t = [
    [None, None],
    ["Yasnaya", "Y"],
    ["Pochinki", "P"],
    ["School", "S"],
    ["Rozhok", "R"],
    ["Farm", "F"],
    ["Mylta", "M"],
    ["Shelter", "H"],
    ["Prison", "I"],
]

returned = LCS(x, y)
# print(returned)

c = returned[0]
t = returned[1]
# print(c)
# print(t)

index = LCS_print(t)

index.reverse()
for item in index:
    writer.write(str(y_t[item][0]) + " ")
writer.write("\n")

# CORRECTNESS
correctness = int((len(index) * 100) / n)
writer.write("Correctness of prediction: " + str(correctness) + "%")
