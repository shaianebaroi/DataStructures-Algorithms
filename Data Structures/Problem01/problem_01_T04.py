#TASK04
#FUNCTION CODE

#USING THE SINGLE-REMOVE-FUNCTION FROM PREVIOUS TASK
def remove(source, size, idx):  
    
    #ENSURING ALL VALUES AFTER SIZE IS ZERO
    count = size
    while (count < (len(source)-1)):
        source[count] = 0
        count += 1
    
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

def removeAll(source,size,element):
    #SEARCHING AND REMOVING MULTIPLE TIMES IN A LOOP
    count2 = 0
    while (count2 >= 0): 
        removed = 0
        count2 = 0
        while (count2 < len(source)):
            if (source[count2] == element) :
                remove (source, size, count2)
                removed += 1
            count2 += 1
        if (removed == 0):
            break
    
    #PRINTING
    print (source)
    
#MAIN CODE
source = [10,2,30,2,50,2,2,0,0]
removeAll (source, 7, 2)