# TASK01

# FUNCTION CODE
def bubbleSort(arr):
    for count in range(len(arr) - 1):
        status = True
        for count2 in range(len(arr) - count - 1):
            if arr[count2] > arr[count2 + 1]:
                # SWAPPING
                temp = arr[count2]
                arr[count2] = arr[count2 + 1]
                arr[count2 + 1] = temp
                status = False
        if status:
            break
    return arr


# MAIN CODE

reader = open("input1.txt", "r")
writer = open("output1.txt", "w")
line = reader.readline()
while line:
    elements = reader.readline().split()
    # print(elements)
    elementsList = [int(item) for item in elements]
    sortedArray = bubbleSort(elementsList)

    # PRINTING THE FIRST N ELEMENTS OF THE SORTED ARRAY
    count = 0
    while count < len(sortedArray):
        writer.write(str(sortedArray[count]) + " ")
        count += 1
    writer.write("\n")
    line = reader.readline()

reader.close()

""" 
The best case scenario in this case would be when a completely sorted array is given as input. As a result, when this happens, no element
is swapped in the entire array. This means that if we initialise a variable (such as status) and assign a boolean value to it (such as True),
each time the program will encounter a swapping of elements, the boolean value of the variable will change (i.e. changes to False). 
However, in the best case, as no swapping occurs within the array, so the boolean value of the variable does not change (i.e. remains True).
"""
