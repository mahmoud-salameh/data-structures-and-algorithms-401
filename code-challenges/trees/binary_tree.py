from re import escape


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):

        output = ''
        if not self.root:
            return 'An emptey tree'

        def traverse(node):
            nonlocal output 
            output += str(node.value) 

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)
                  
        traverse(self.root)

        return output
    
    def post_order(self):
        output = ''
        if not self.root:
            return 'An emptey tree'
        
        def traverse(node):
            nonlocal output 

            if node.left:
                
                traverse(node.left)
                
            if node.right:
                traverse(node.right)

            output += str(node.value)       

        
        traverse(self.root)
         
        return output

    def in_order(self):
        output = ''
        if not self.root:
            return 'An emptey tree'
        
        def traverse(node):
            nonlocal output 

            if node.left:
                
                traverse(node.left)

            output += str(node.value)
                
            if node.right:
                traverse(node.right)

        traverse(self.root)
         
        return output






