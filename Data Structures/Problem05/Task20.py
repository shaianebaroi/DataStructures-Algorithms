#================================ NODE CLASS =================================
class Node:
    def __init__ (self, element, next):
        self.element = element
        self.next = next
        
    def printNode (self):
        print (self.element, "-", self.next)
        
#============================ LINKED LIST CLASS ==============================
class MyList():
    def __init__ (self, source):
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
                
    def showList (self):
        n = self.head
        if (n == None):
            print ("Empty List")  
        while (n != None):
            n.printNode()
            n = n.next
            
    def remove (self, deleteKey):
        status = False
        n = self.head
        while (n != None):
            
            if (n.element == deleteKey):
                status = True
                #COPYING THE VALUES OF THE NEXT NODE INTO THIS NODE
                n2 = n
                n = n.next
                n2.element = n.element
                #COPYING THE ADDRESS OF THE NODE AFTER THE DELETED
                n2.next = n.next   
                self.showList()
                return (deleteKey)
                break
            else:
                status = False
                n = n.next
        
        if status == False:
            print ("The key was not found!")
        
        self.showList()

#=============================== TESTER CLASS ================================
list1 = [20, 40, 60, 80, 100]

list01 = MyList(list1)
list01.remove(10)
