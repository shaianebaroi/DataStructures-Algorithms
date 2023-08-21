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

#TASK03
#FUNCTION CODE
def remove(source, size, idx):    
    #ENSURING ALL VALUES AFTER SIZE IS ZERO
    count = size
    while (count < (len(source)-1)):
        source[count] = 0
        count += 1
    #print (source)
    
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
    
#TASK06
#FUNCTION CODE

def array_series (n):
    #NEW ARRAY TO STORE DATE, ARRAY SIZE to n^2
    store = []
    count = 0
    while (count < n):
        count2 = 0
        while (count2 < n):
            store += [0]
            count2 += 1
        count += 1
    
    #TRAVERSED THE ARRAY IN GROUPS OF N
    #NTH ELEMENT TO 0TH ELEMENT OF THAT GROUP
    #SET VALUES FROM 1 TO N
    count = 1
    while (count < (n + 1)):
        count2 = 1
        while (count2 < count + 1):            
            store [count*n - count2] =count2
            count2 += 1
        count += 1
        
    #PRINTING    
    print(store)

#TASK07
#FUNCTION CODE
def bunch (source):
    
    #CREATING A TEMPORARY VARIBLE TO STORE INITIAL VALUES FOR COMPARISON
    count = 0
    while (count < len(source)):
        temp = source[count]
        
        #COMPARING AND THEN COUNTING THE MAXIMUM OF EACH REPEATED DIGITS 
        maximum = 1
        while (count < len(source) - 1):
            
            if temp == source[count + 1]:
                maximum += 1
                count += 1
                continue
            else:
                break
            
        count += 1
        
    print(maximum)

#MAINCODE07
source07 = [1, 2, 2, 3, 4, 4, 4]
bunch (source07)

#MAINCODE06
array_series (4)

#MAINCODE05
source05 = [10, 3, 1, 2, 10]
balance(source05)
    
#MAINCODE04
source04 = [10,2,30,2,50,2,2,0,0]
removeAll (source04, 7, 2)

#MAINCODE03
source03 = [10, 20, 30, 40, 50, 0, 0]
remove (source03, 5, 2)       
      
#MAINCODE02
source02 = [10, 20, 30, 40, 50, 60, 70]
rotateLeft (source02, 4)

#MAINCODE01
source01 = [10, 20, 30, 40, 50]
shiftLeft (source01, 3)