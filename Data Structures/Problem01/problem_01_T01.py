#TASK01
#FUNCTION CODE
def shiftLeft (source, k):
          
    #SHIFTING-LEFT   
    count1 = 0;  
    count2 = k; 
    while (count2 <= len(source) - 1):
        source[count1] = source[count2];
        count1 += 1
        count2 += 1
    
    #REPLACING
    count = len(source) - k;
    while (count < len (source)):
        source[count] = 0;
        count += 1;        
    
    #PRINTING
    print(source)

#MAINCODE01
source = [10, 20, 30, 40, 50]
shiftLeft (source, 3)