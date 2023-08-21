#TASK01
#FUNCTION CODE

def reverse (source):
    
    count2 = 0
    count = len(source) - 1
    new_list = [0] * (count + 1)
    while (count >= 0):
        new_list[count2] = source[count]
        count2 += 1
        count -= 1
    print (new_list)

#MAIN CODE    
source = [10,20,30,40,50,60,70,80,90,100]
reverse (source)
    