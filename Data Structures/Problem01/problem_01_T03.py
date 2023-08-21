#TASK03
#FUNCTION CODE
def remove(source, size, idx):    
    
    #ENSURING ALL VALUES AFTER SIZE IS ZERO
    count = size
    while (count < (len(source)-1)):
        source[count] = 0
        count += 1
    print (source)
    
    #SHIFTING CELLS LEFT FROM THE POINT OF IDX
    count1 = idx
    count2 = idx + 1
    
    #SHIFTING
    while (count2 <= len(source) - 1):
        source[count1] = source[count2];
        count1 += 1
        count2 += 1
        
    #REPLACING WITH ZERO  
    count = len(source) - 1;
    while (count < len (source)):
        source[count] = 0;
        count += 1;
    
    #PRINTING
    print (source)

#MAIN CODE
source = [10, 20, 30, 40, 50, 0, 0]
remove (source, 5, 2)