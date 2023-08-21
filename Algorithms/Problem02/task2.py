# TASK02

# FUNCTION CODE


def selectionSort(elementList):
    pointer = 0
    # TRAVERSING THE POINTER THROUGH THE ARRAY
    while pointer < len(elementList):

        # FINDING THE MINIMUM
        swapping = False
        count = pointer + 1
        minimum = elementList[pointer]
        while count < len(elementList):
            if elementList[count] < minimum:
                minimum = elementList[count]
                minLocation = count
                swapping = True
            count += 1
        # print (minimum)

        # SWAPPING
        if swapping == True:
            temp = elementList[minLocation]
            elementList[minLocation] = elementList[pointer]
            elementList[pointer] = temp

        pointer += 1

    return elementList


# MAIN CODE

# TAKING INPUT
reader = open("input2.txt", "r")
writer = open("output2.txt", "w")
line = reader.readline()
while line:
    elements = reader.readline().split()
    prices = reader.readline().split()
    # print(elements)
    # print(prices)
    elementsList = [int(item) for item in elements]
    pricesList = [int(item) for item in prices]
    sortedArray = selectionSort(pricesList)

    # PRINTING THE FIRST N ELEMENTS OF THE SORTED ARRAY
    limit = elementsList[1]
    count = 0
    while count < limit:
        writer.write(str(sortedArray[count]) + " ")
        count += 1
    writer.write("\n")
    line = reader.readline()

reader.close()
