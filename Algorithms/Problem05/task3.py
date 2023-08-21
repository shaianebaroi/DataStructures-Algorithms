# ============================= FUNCTION CODE ==================================
import heapq


def Jack_and_Jill(t, hours, call):
    hours.sort()
    # print(hours)

    hours_Jack = 0
    hours_Jill = 0
    all = []
    Jack = [0] * t  # PRIORITY QUEUE USING MAX-HEAP
    Jill = [0] * t

    for count in range(0, len(call)):
        if call[count] == "J":
            time = int(hours.pop(0))
            hours_Jack += time
            # JACK'S TIMES GET HEAP SORTED IN DESCENDING ORDER SO THAT JILL CAN TAKE THE TASK WITH THE LONGEST TIME
            # TAKING NEGATIVE VALUES SORTS IN MAX-HEAP
            heapq.heappush(Jack, -1 * time)
            all.append(time)

        if call[count] == "j":
            # AS JACK'S TIMES ARE SORTED IN MAX-HEAP, THE TASK WITH LONGEST TIME IS ALWAYS AT INDEX 0
            # SO JILL'S TIME IS THE POPPED VALUE FROM JACK'S TIMES
            # THE NEGATIVE VALUE IS TURNED BACK INTO POSITIVE
            time2 = int(heapq.heappop(Jack)) * -1
            hours_Jill += time2
            Jill.append(time2)
            all.append(time2)
        
        

    # PRINTING
    for count in range(0, len(all)):
        writer.write(str(all[count]) + "")
    writer.write("\n")
    writer.write("Jack will work for " + str(hours_Jack) + " hours")
    writer.write("\n")
    writer.write("Jill will work for " + str(hours_Jill) + " hours")


# ============================= DRIVER CODE ==================================
reader = open("task3_input.txt", "r")
writer = open("task3_output.txt", "w")

no_of_tasks = reader.readline()
t = int(no_of_tasks)
val = reader.readline()
hours = list(map(str, val.split()))
call = reader.readline()
# print(t, hours, call)

Jack_and_Jill(t, hours, call)
