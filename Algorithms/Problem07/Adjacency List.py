# from array import *

reader = open("input1.txt", "r")

# TAKING THE DIMENSION FOR THE MATRIX
n = reader.readline()
# print(n)
d = int(n)

# INPUTTING VALUES FROM EACH LINE IN A LIST AS STRING
aList = []
for line in reader:
    l = line
    # MAP FUNCTION FILTERS UNNECESSARY SPACES AND ALLOWS TO SPLIT INTO A GIVEN DATA TYPE
    val = list(map(str, l.split()))
    # print(val)
    aList.append(val)

print(aList)

reader.close()
