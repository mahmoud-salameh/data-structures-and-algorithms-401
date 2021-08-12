
from stack_and_queue.stack_and_queue import*
from re import escape


def is_match(a1,a2):
    if a1 == '(' and a2 ==')':
        return True
    elif a1 == '{' and a2 == '}':
        return True
    elif a1 == '[' and a2 == ']':
        return True
    else:
        return False


def the_paran_balanced(paren_staing):
    stack = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_staing) and is_balanced:
        paren = paren_staing[index]
        if paren in '([{':
            stack.push(paren)
        else:
            if stack.isEmpty():
                is_balanced= False
            else:
                tob = stack.pop()
                if not is_match(tob, paren):
                    is_balanced =False
        index += 1

    if stack.isEmpty() and is_balanced:
        return True
    else:
        return False







# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def pre_order(self):

#         output = ''
#         if not self.root:
#             return 'The Tree is empty'

#         def traverse(node):
#             nonlocal output 
#             output += str(node.value) 

#             if node.left:
#                 traverse(node.left)

#             if node.right:
#                 traverse(node.right)
                  
#         traverse(self.root)

#         return output
    
#     def post_order(self):
#         output = ''
#         if not self.root:
#             return 'The Tree is empty'
        
#         def traverse(node):
#             nonlocal output 

#             if node.left:
                
#                 traverse(node.left)
                
#             if node.right:
#                 traverse(node.right)

#             output += str(node.value)       

        
#         traverse(self.root)
         
#         return output

#     def in_order(self):
#         output = ''
#         if not self.root:
#             return 'The Tree is empty'
        
#         def traverse(node):
#             nonlocal output 

#             if node.left:
                
#                 traverse(node.left)

#             output += str(node.value)
                
#             if node.right:
#                 traverse(node.right)

#         traverse(self.root)
         
#         return output



# class BinarySearchTree(BinaryTree):

#     def add(self,value):

#         if self.root ==None:
#             self.root=Node(value)
#         else:
#             node = Node(value)

#             def traverse(root):
#                 if node.value < root.value:

#                     if root.left:
#                         root=root.left
#                         traverse(root)
#                     else:
#                         root.left=node
#                 else:

#                     if root.right:
#                         root=root.right
#                         traverse(root)
#                     else:
#                         root.right=node

#             traverse(self.root)
    
#     def contains(self,value):
#         x=False
#         if self.root ==None:
#             return 'The Tree is empty'
#         else:
#             def traverse(root):
                
#                 if root.value==value:
#                     nonlocal x
#                     x=True
#                 if root.value>value:
#                     if not root.left:
#                         return

#                     if root.left.value==value:
#                         x= True
#                     else:
#                         traverse(root.left)
#                 if root.value<value:
#                     if not root.right:
#                         return
#                     if root.right.value==value:
#                         x= True
#                     else:
#                         traverse(root.right)


#             traverse(self.root)

#             return x



          
# if __name__ == "__main__":
#     tree= BinarySearchTree()
#     tree.add(8)
#     tree.add(4)
#     tree.add(7)
#     tree.add(3)

#     print(tree.root.left.left.value)
#     print(tree.contains(12))