#TASK01

#------------------------------- NODE CLASS --------------------------------
class Node:
    
    def __init__ (self, element = None, next = None):
        self.element = element
        self.next = next
        
    def printNode (self):
        print (self.element, "-", self.next)
        
#---------------------------- LINKED LIST CLASS ----------------------------- 

#TASK02 
        
class MyList:
    
    #CONSTRUCTORS 
    def __init__ (self, source = None):
        
        #1(A) USING NO PARAMETERS           
        if (source == None): 
            self.head = None
        
        #1(B) USING ARRAY AS A PARAMETER 
        elif (type(source) == type(list())):
            self.head = None
            tail = None 
              
            count = 0
            while (count < len(source)):            
                n = Node (source[count], None)
                
                if (self.head == None):
                    self.head = n
                    tail = n                    
                else:
                    tail.next = n
                    tail = n
                    
                count += 1
        
        #1(C) USING ANOTHER LIST AS A PARAMETER 
        elif (type(source) == type(Node())):
            #print ("object")
            self.head = source
            
        elif (type(source) == type(MyList())):
            self.head = source.head