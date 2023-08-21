#TASK 07
#FUNCTION CODE
def insertion (source, index, value, size):
    
    #VALIDATION CHECKS
    status = True
    
    #CHECKING IF THE ARRAY IS FULL OR NOT
    if (size == len(source)):
        print ("No space in array!")
        status = False
    #print (status)
    
    #CHECKING IF INDEX IS NEGATIVE OR OUT OF RANGE
    if (status == True):
        if (index < 0 or index > size):
            print ("Invalid index")
            status = False    
        #print (status)
    
    #INSERTION
    if (status == True):         
        #RIGHT SHIFTING
        count = size - 1
        while (count >= index):
            source[count + 1] = source [count]
            count -= 1
        
        #print (source)
        
        #REPLACING
        source[index] = value
        
        print (source)
    
#MAIN CODE
source = [10, 20, 30, 40, 50, 0, 0, 0]
insertion (source, 2, 200, 5)