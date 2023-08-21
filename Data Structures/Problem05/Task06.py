#TASK06
#FUNCTION CODE

def rightRotate (source, k):
    
    #STORING THE LAST K VALUES
    temp = [0] * k
    count = len(source) - k
    count2 = 0
    while (count < len(source)):
        temp[count2] = source[count]
        count += 1
        count2 += 1
    
    #print (temp)
    
    #SHIFTING
    count = len(source) - 1
    while (count > 0):
        source[count] = source[count-k]
        count -= 1
    
    #REPLACING FIRST VALUE WITH LAST VALUE
    
    count2 = 0
    while (count < len(temp)):
        source[count] = temp[count]
        count += 1

    print (source)
    
#MAIN CODE    
source = [10,20,30,40,50,60,70,80,90,100]
rightRotate (source, 3)
    

