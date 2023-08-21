#TASK10
#FUNCTION CODE

def array_output (source, index, size):
    
    count = (index + (size - 1)) % len(source)
    count2 = 0
    print (count)
    while (count2 < size):
        print (source[count])
        count -= 1
        count2 += 1
        
    if (index < 0):
        count = len(source) - 1
        
#MAIN CODE
source = [40, 50, 0, 0, 0, 0, 0, 0, 10, 20, 30] 
array_output (source, 8, 5)
