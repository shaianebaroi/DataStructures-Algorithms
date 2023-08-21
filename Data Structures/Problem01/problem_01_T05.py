#TASK05
#FUNCTION CODE

def balance(source):    
    #SUMMATION FOR LEFT PAN
    count = 0
    leftpan = 0
    rightpan = 0
    while (count < len(source)):
        leftpan += source[count]
        
        #SUMMATION FOR RIGHT PAN
        count2 = count + 1
        while (count2 < len(source)):
            rightpan += source[count2]
            count2 += 1
        count += 1
        
        #CONDITIONS FOR TRUE AND FALSE
        if (leftpan == rightpan):
            point = 1
            break
        else:
            point = 0

        rightpan = 0
    
    #FINAL CONDITIONS
    if (point == 1):
        print ("true")
    else:
        print ("false")

#MAIN CODE
source = [10, 3, 1, 2, 10]
balance(source)