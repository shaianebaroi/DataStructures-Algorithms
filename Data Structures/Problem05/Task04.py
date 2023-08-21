#TASK04
#FUNCTION CODE

def rightRotate (source):
    
    #STORING THE LAST VALUE
    temp = source[len(source) - 1]
    
    #SHIFTING
    count = len(source) - 1
    while (count > 0):
        source[count] = source[count-1]
        count -= 1
    
    #REPLACING FIRST VALUE WITH LAST VALUE
    source[0] = temp
    print (source)
    
#MAIN CODE    
source = [10,20,30,40,50,60,70,80,90,100]
rightRotate (source)
    

