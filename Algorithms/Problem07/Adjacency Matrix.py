from array import *

reader = open("input1.txt", "r")

# TAKING THE DIMENSION FOR THE MATRIX
n = reader.readline()
# print(n)
d = int(n)

# CREATING AND POPULATING THE MATRIX OF DIMENSION N WITH NULL VALUES
matrix = []
for count in range(d):
    a = []
    for count2 in range(d):
        a.append(0)
    matrix.append(a)
# print(matrix)

# INPUTTING VALUES FROM EACH LINE IN A LIST AS STRING
for line in reader:
    l = line
    # MAP FUNCTION FILTERS UNNECESSARY SPACES AND ALLOWS TO SPLIT INTO A GIVEN DATA TYPE
    val = list(map(str, l.split()))
    print(val)
    row = int(val[0][0])
    column = int(val[1][0])
    matrix[row][column] = 1  # USED AS THE ITERATIVE VARIABLE

reader.close()

# CONVERTING TO LIST
for count in range(len(matrix)):
    for count2 in range(len(matrix)):
        print(matrix[count][count2], end=" ")
    print()
