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

    def counting (self):
        count = 0
        n = self.head
        while (n != None):
            count += 1
            n = n.next
        return count

#=============================== TESTER CLASS ================================
list1 = [20, 40, 60, 80, 100]

list01 = MyList(list1)
print(list01.counting())