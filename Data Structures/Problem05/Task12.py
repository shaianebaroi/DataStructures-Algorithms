#TASK12
#FUNCTION CODE

def circular_to_linear (source, size, index):

    n = len(source)
    list1 = [0] * n
    
    count = 0
    while (count < size):
        list1[count] = source[index]
        index = (index + 1) % len(list1)
        count += 1
        
    print (list1)
        
    
#MAIN CODE
source = [40, 50, 0, 0, 0, 0, 0, 0, 10, 20, 30]
circular_to_linear (source, 5, 8)