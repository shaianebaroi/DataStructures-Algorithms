#TASK13
#FUNCTION CODE

def resize_linear (source, size):

    list1 = [0] * size
    
    count = 0
    while (count < len(source)):
        list1[count] = source[count]
        count += 1
        
    source = list1
    
    print (source)
        
    
#MAIN CODE
source = [10, 20, 30, 40, 50]
resize_linear (source, 7)