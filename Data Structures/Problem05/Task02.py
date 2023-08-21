#TASK02
#FUNCTION CODE

def reverse (source):
    
    #SWAPPING
    count = 0
    count2 = len(source) - 1
    temp = 0
    while (count2 > count):
        temp = source[count]
        source[count] = source[count2]
        source[count2] = temp
        count += 1
        count2 -= 1

    print (source)
    
#MAIN CODE    
source = [10,20,30,40,50,60,70,80,90,100]
reverse (source)
    