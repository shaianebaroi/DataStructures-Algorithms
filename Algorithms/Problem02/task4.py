def mergeSort(array):
    if len(array) == 1:
        return array
    else:
        mid = int(len(array) / 2)
        array1 = mergeSort(array[:mid])
        array2 = mergeSort(array[mid:])
        new_arr = []
        pointer1 = 0
        pointer2 = 0
        for a in range(len(array)):
            if array1[pointer1] < array2[pointer2]:
                new_arr.append(array1[pointer1])
                pointer1 += 1
            elif array1[pointer1] > array2[pointer2]:
                new_arr.append(array2[pointer2])
                pointer2 += 1
            else:
                new_arr.append(array1[pointer1])
                pointer1 += 1
                new_arr.append(array2[pointer2])
                pointer2 += 1
            if pointer1 >= len(array1):
                new_arr += array2[pointer2:]
                break
            elif pointer2 >= len(array2):
                new_arr += array1[pointer1:]
                break
        return new_arr


# MAIN CODE

reader = open("input4.txt", "r")
writer = open("output4.txt", "w")
line = reader.readline()
while line:
    elements = reader.readline().split()
    # print(elements)
    elementsList = [int(item) for item in elements]
    sortedArray = mergeSort(elementsList)

    # PRINTING THE FIRST N ELEMENTS OF THE SORTED ARRAY
    count = 0
    while count < len(sortedArray):
        writer.write(str(sortedArray[count]) + " ")
        count += 1
    writer.write("\n")
    line = reader.readline()

reader.close()
