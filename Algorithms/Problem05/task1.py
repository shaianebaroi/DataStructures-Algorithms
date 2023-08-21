# ============================= FUNCTION CODE ==================================
def sorting(arr):
    # SORTING THE ARRAY IN ASCENDING ORDER OF ENDING TIMES
    for count in range(0, len(arr)):
        min = int(arr[count][1])
        minLocation = count
        for count2 in range(count + 1, len(arr)):
            limit = int(arr[count2][1])
            if limit <= min:
                min = int(arr[count2][1])
                minLocation = count2

        # SWAPPING
        temp = arr[count]
        arr[count] = arr[minLocation]
        arr[minLocation] = temp

    return arr


def comparison(arr):
    # COMPARING START AND END TIMES
    start = int(arr[0][0])
    end = int(arr[0][1])
    final = [[str(start), str(end)]]
    for count in range(0, len(arr)):
        start1 = int(arr[count][0])
        end1 = int(arr[count][1])
        if start1 >= end:
            start = end
            end = int(arr[count][1])
            final.append(arr[count])
    return final


def Assignment_Selection(arr, n):

    array = sorting(arr)
    # print(array)
    final = comparison(array)

    # PRINTING THE COUNT
    writer.write(str(len(final)) + "\n")

    # PRINTING THE ARRAY
    for count in range(len(final)):
        writer.write(str(final[count][0]) + " " + str(final[count][1]))
        writer.write("\n")


# ============================= DRIVER CODE ==================================
reader = open("task1_input.txt", "r")
writer = open("task1_output.txt", "w")

no_of_assignments = reader.readline()
n = int(no_of_assignments)
# print(n)

arr = []
for count in range(0, n):
    val = reader.readline()
    times = list(map(str, val.split()))
    arr.append(times)
# print(arr)

Assignment_Selection(arr, n)
