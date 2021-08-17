class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        self.list_in_tree = []

    def print_trees(self, traversal_type):
        if traversal_type == 'preorder':
            return self.pre_order_print(tree.root, '')
        elif traversal_type == 'inorder':
            return self.in_order_print(tree.root, '')
        elif traversal_type == 'postorder':
            return self.post_order_print(tree.root, '')
        else:
            print('Travesal type ' + str(traversal_type) + 'is not supported.')
            return False
            
    def pre_order_print(self):
        output = ''
        def traversal(node):
            nonlocal output 
            output += str(node.data) 
            self.list_in_tree+=[(node.data)]
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)
        traversal(self.root)
        return output

    def in_order_print(self):
        output = ''
        def traversal(node):
            nonlocal output 
            if node.left:
                traversal(node.left)
            output += str(node.data)
            if node.right:
                traversal(node.right)
        traversal(self.root)
        return output


    def post_order_print(self):
        output = ''
        def traversal(node):
            nonlocal output 
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)
            output += str(node.data)       
        traversal(self.root)
        return output

    def max_in_tree(self):
        self.max = 0
        def traversal(node):
            if node.left:
                traversal(node.left)
                if node.left.data > self.max:
                    self.max = node.left.data
            if node.right:
                traversal(node.right)
                if node.right.data > self.max:
                    self.max = node.right.data
        
        traversal(self.root)
        if self.root.data > self.max:
            return self.root.data
        return self.max
       
    def breadth_first(tree):
        in_queue = [tree.root]
        breadth = []
        if not tree.root:
            return []
    
        while in_queue:

            node = in_queue[0]
            if node.left != None:
                in_queue += [node.left]
                
            if node.right != None:
                in_queue += [node.right]

            breadth += [in_queue[0].data]
            in_queue = in_queue[1:]
        return breadth
    


class k_Ary:
   def fizz_buzz_tree(self, kAryTree):
      result = []
      for i in range(1, kAryTree +1):
         if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
         elif i %3==0:
            result.append("Fizz")
         elif i% 5 == 0:
            result.append("Buzz")
         else:
            result.append(str(i))
      return result














# ob1 = k_Ary()
# print(ob1.fizz_buzz_tree(100))
       
       
        #                  3
        #                /   \
        #              4       11
        #             / \     / \
        #            1   13       19
        #                 \     
        #                  23  

# if __name__ == "__main__":
#     tree = BinaryTree()
#     tree.root = Node(3)
#     tree.root.left = Node(4)
#     tree.root.right = Node(11)
#     tree.root.left.left = Node(1)
#     tree.root.left.right = Node(13)
#     tree.root.left.right.right = Node(23)
#     tree.root.right.right = Node(19)
#     print(tree.breadth_first())