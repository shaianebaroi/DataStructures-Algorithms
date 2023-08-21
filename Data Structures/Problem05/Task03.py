#TASK03
#FUNCTION CODE

def rightShift (source):
    
    #SHIFTING
    count = len(source) - 1
    while (count > 0):
        source[count] = source[count-1]
        count -= 1
        
    #REPLACING VALUES WITH ZERO
    source[0] = 0
    
    print (source)
    
#MAIN CODE    
source = [10,20,30,40,50,60,70,80,90,100]
rightShift (source)
    

