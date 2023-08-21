# ====================================== FUNCTION CODE ===========================================


def LCS(x, y, z):
    m = len(x) + 1
    n = len(y) + 1
    o = len(z) + 1

    c = [[[0] * (n) for i in range(m)] * (o) for j in range(m)]
    t = [[[None] * (n) for i in range(m)] * (o) for j in range(m)]

    max = 0
    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                    t[i][j][k] = None
                else:
                    if x[i - 1] == y[j - 1] and x[i - 1] == z[k - 1]:
                        c[i][j][k] = 1 + c[i - 1][j - 1][k - 1]
                        t[i][j][k] = "diagonal"

                    else:
                        if c[i - 1][j][k] >= c[i][j - 1][k]:
                            max = c[i - 1][j][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                                t[i][j][k] = "up-up-left"
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max
                                t[i][j][k] = "left-up-up"
                        else:
                            max = c[i][j - 1][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                                t[i][j][k] = "up-left-up"
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max
                                t[i][j][k] = "left-up-up"

    return c[len(c) - 1][len(c) - 1][len(c) - 1]


# ======================================  DRIVER CODE  ===========================================

reader = open("input2.txt", "r")
writer = open("output2.txt", "w")
x = reader.readline().rstrip()
y = reader.readline().rstrip()
z = reader.readline().rstrip()

length = LCS(x, y, z)
writer.write(str(length))
