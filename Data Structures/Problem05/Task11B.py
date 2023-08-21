#TASK11-B
#FUNCTION CODE

def linear_to_circular (source, size, index):

    n = len(source)
    list1 = [0] * n
    
    count = 0
    while (count < size):
        list1[index] = source[count]
        index = (index + 1) % len(list1)
        count += 1
        
    print (list1)
        
    
#MAIN CODE
source = [10, 20, 30, 40, 50, 0, 0, 0, 0, 0, 0]
linear_to_circular (source, 5, 8)