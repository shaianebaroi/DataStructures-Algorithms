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


def Assignment_Selection(arr, n, p):

    array = sorting(arr)
    q = []
    for count in range(0, p):
        out = array.pop(0)
        q.append(out)
    # print(q)
    # print(array)

    final = []
    counter = 0
    for count in range(0, p):
        # INSERTING THE INITIAL POPPED TASK FOR EACH PERSON
        array.insert(0, q[count])
        tasks = comparison(array)
        final.append(tasks)
        for count2 in range(0, len(tasks)):
            # REMOVING THE TASKS ALREADY DONE BY A PERSON
            array.remove(tasks[count2])
            counter += 1
    # print(final)
    writer.write(str(counter))


# ============================= DRIVER CODE ==================================
reader = open("task2_input.txt", "r")
writer = open("task2_output.txt", "w")

val = reader.readline()
line = list(map(str, val.split()))
# print(line)
no_of_assignments = line[0]
no_of_people = line[1]
n = int(no_of_assignments)
p = int(no_of_people)
# print(n)
# print(p)

arr = []
for count in range(0, n):
    val = reader.readline()
    times = list(map(str, val.split()))
    arr.append(times)
# print(arr)

Assignment_Selection(arr, n, p)
