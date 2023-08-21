#TASK11-A
#FUNCTION CODE

def linear_to_circular (source, size, index):

    #SHIFTING
    count = index
    count2 = 0
    while (count < len(source)):
        source[count] = source[count2]
        source[count2] = 0
        count += 1
        count2 += 1      
    
    #print (source)
    
    count = 0
    count2 = 0
    while (count < index):
        if (source[count] != 0):
            source[count2] = source[count]
            source[count] = 0
            count2 += 1
        count += 1
    print (source)
    
#MAIN CODE
source = [10, 20, 30, 40, 50, 0, 0, 0, 0, 0, 0]
linear_to_circular (source, 5, 8)