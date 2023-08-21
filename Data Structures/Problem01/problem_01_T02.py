#TASK02
#FUNCTION CODE
def rotateLeft (source,k):
    
    #INITIALISING VALUES WITH ZERO IN THE TEMPORARY ARRAY
    temp = [0] * k
    
    #COPYING VALUES TO THE TEMPORARY ARRAY
    count = 0
    while (count < k):
        temp[count] = source[count]
        count += 1
        
    #LEFT-SHIFTING
    count1 = 0
    count2 = k
    while (count2 <= len(source) - 1):
        source[count1] = source[count2];
        count1 += 1
        count2 += 1
    
    #RETRIEVING VALUES FROM TEMPORARY ARRAY
    count1 = len(source) - k;
    count2 = 0
    while (count1 < len (source)):
        source[count1] = temp[count2];
        count1 += 1        
        count2 += 1
    
    #PRINTING
    print(source)        
      
#MAIN CODE
source = [10, 20, 30, 40, 50, 60, 70]
rotateLeft (source, 4)