#TASK09-B
#FUNCTION CODE

def array_output (source, size, index):
    
    count = 0
    while (count < size):
        print (source[index])
        index = (index + 1) % len(source)
        count += 1

#MAIN CODE
source = [40, 50, 0, 0, 0, 0, 0, 0, 10, 20, 30] 
array_output (source, 5, 8)
