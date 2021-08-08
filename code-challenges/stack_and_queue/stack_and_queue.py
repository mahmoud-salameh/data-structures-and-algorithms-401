class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        try:
           popValue = self.top.value
           self.top = self.top.next
           return popValue
        except:
            return "An empty stack"

    def peek(self):
        try:
            return self.top.value
        except:
            return "An empty stack"

    def isEmpty(self):
        return self.top == None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        node  =  Node(value)
        if not self.front:
            self.front  =  node
            self.rear  =  node
        else:
            self.rear.next  =  node
            self.rear  =  node
    
    def dequeue(self):
        try:
           dequeue_input = self.front.value
           self.front = self.front.next
           return dequeue_input
        except :
           return "An empty Queue"

    def peek(self):
        try:
           return self.front.value
        except :
            return "An empty Queue"

    def isEmpty(self):
        return self.front  ==  None
        

""" ---------------------------------------------stack-queue-pseudo tests---------------------------------------------------- """
    
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,value):
        node = Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        try:
           popValue = self.top.value
           self.top = self.top.next
           return popValue
        except:
            return 'An empty stack'

    def peek(self):
        try:
            return self.top.value
        except:
            return 'An empty stack'

    def isEmpty(self):
        return self.top == None

class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()
    
    def enqueue(self,value=None):
        if value == None:
            return 'Please put a value'
    
        self.front.push(value)
        
    def dequeue(self):
        
        if not self.front.top:
            return 'The Queue is empty'
           
        while self.front.top:
            
       
            self.rear.push(self.front.pop())

        dequeue_value = self.rear.pop()

        while self.rear.top:
        
    
            self.front.push(self.rear.pop())

        return dequeue_value

            
    
