#TASK 08
#FUNCTION CODE
def remove (source, index, size):
    
    #VALIDATION CHECKS
    status = True
       
    #CHECKING IF INDEX IS NEGATIVE OR OUT OF RANGE
    if (status == True):
        if (index < 0 or index >= len(source) - 2):
            print ("Invalid index")
            status = False    
        #print (status)
    
    #REMOVING
    if (status == True):
        source [index] = 0
         
        #LEFT-SHIFTING
        count = index + 1
        while (count < len(source)):
            source[count - 1] = source [count]
            count += 1
        
        print (source)
    
#MAIN CODE
source = [10, 20, 30, 40, 50, 0, 0, 0]
remove (source, 2, 5)