#TASK14
#FUNCTION CODE

def resize_circular (source, size, index):

    list1 = [0] * (size + 2)
    
    count = index
    count2 = 0
    while (count2 < size):
        list1[count] = source[index]
        index = (index + 1) % len(source)
        count = (count + 1) % len(list1)
        count2 += 1
        
        
    source = list1
    
    print (source)
        
    
#MAIN CODE
source = [20, 30, 40, 50, 10]
resize_circular (source, 5, 4)