#TASK01

#================================DESIGN CLASS=================================
class Parenthesis_Balancing: 
    def __init__ (self):
        self.stack = []
        
    def peek (self):
        length = len(self.stack)
        if (length > 0):
            return self.stack[-1]
        else:
            return None
        
    def push (self, value):
        self.stack.append(value)
        
    def pop(self):
        self.stack.pop(-1)

def checker (expression):
    
    stack = Parenthesis_Balancing()
    
    #KEEPING TWO LISTS WITH THE OPENING AND CLOSING BRACKETS
    open_brackets = ["(", "{", "["]
    close_brackets = [")", "}", "]"]
    
    #SEARCHING FOR THE FIRST OPENING BRACKET AND PUTTING IT IN THE STACK
    length = len(expression)
    status = False
    count = 0
    while (count < length):
        element = stack.peek()
        if (expression[count] == open_brackets[0]) or (expression[count] == open_brackets[1]) or (expression[count] == open_brackets[2]):
            stack.push(count)
        
        #LOOKING FOR THE CLOSING BRACKET OF THE FOUND OPEN BRACKET    
        elif (expression[count] == close_brackets[0]) or (expression[count] == close_brackets[1]) or (expression[count] == close_brackets[2]):
            if (element != None):
                #CHECKING FOR THE CORRESPONDING CLOSE BRACKET OF THE FOUND BRACKET
                 if (expression[count] == close_brackets[0] and expression[element] == open_brackets[0]) or (expression[count] == close_brackets[1] and expression[element] == open_brackets[1]) or (expression[count] == close_brackets[2] and expression[element] == open_brackets[2]):
                    stack.pop()
            
            #IF THERE IS NO ELEMENT IN THE STACK
            else:
                status = True
                print("This expression is NOT correct.")
                print("Error at character" + str(count + 1) + "." + str(expression[count]) + "- not opened.")
                break
        count += 1
    
    #PRINTING CONDITIONS
    element = stack.peek()
    if (element != None):
       status = True
       print("This expression is NOT correct.")
       print("Error at character" + str(element + 1) + "." + str(expression[element]) + "- not closed.")
       
    if (status == False):
       print("This expression is correct.")

#=================================TESTER CLASS================================
checker ("1+2*(3/4)")
checker ("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
checker ("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
checker ("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
