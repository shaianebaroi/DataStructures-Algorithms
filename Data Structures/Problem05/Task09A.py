#TASK09-A
#FUNCTION CODE

def array_output (source, size, index):
    
    count = 0
    while (count < size):
        print (source[index])
        index += 1
        count += 1
        if (index >= len(source)):
            index = 0

#MAIN CODE
source = [40, 50, 0, 0, 0, 0, 0, 0, 10, 20, 30] 
array_output (source, 5, 8)
