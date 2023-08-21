# FUNCTION CODE


def insertionSort(elementsList):
    count = 0
    while count < len(elementsList) - 1:
        temp = elementsList[count + 1]

        count2 = count
        while count2 >= 0:
            if elementsList[count2] > temp:
                elementsList[count2 + 1] = elementsList[count2]
            else:
                break
            count2 -= 1
        elementsList[count2 + 1] = temp
        count += 1
    return elementsList


# MAIN CODE
# TAKING INPUT
reader = open("input3.txt", "r")
line = reader.readline()
# PRINTING THE FIRST N ELEMENTS OF THE SORTED ARRAY
writer = open("output3.txt", "w")
while line:
    studentsID = reader.readline().split()
    element = reader.readline().split()
    elementsList = [int(item) for item in element]
    elementList = elementsList.copy()
    studentsIDList = [int(item) for item in studentsID]
    sortedArray = insertionSort(elementsList)
    # print(studentsIDList)
    # print(elementList)
    # print(sortedArray)

    studentsID = []
    count = len(sortedArray) - 1
    while count >= 0:
        count2 = 0
        while count2 < len(sortedArray):
            if sortedArray[count] == elementList[count2]:
                index = count2
                studentsID.append(studentsIDList[index])
                # studentsIDList[count2] = 0
                elementList[count2] = 0
            count2 += 1
        count -= 1

    # print(studentsID)

    count = 0
    while count < len(studentsID):
        print(str(studentsID[count]), end=" ")
        writer.write(str(studentsID[count]) + " ")
        count += 1
    print("")
    writer.write("\n")
    line = reader.readline()

reader.close()
writer.close()
