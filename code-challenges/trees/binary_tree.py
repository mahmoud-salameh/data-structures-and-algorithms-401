class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

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
        if not self.root:
                return 'An emptey tree'
        def traversal(node):
            nonlocal output 
            output += str(node.data) 
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)
        traversal(self.root)
        return output

    def in_order_print(self):
        output = ''
        if not self.root:
            return 'An emptey tree'
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
        if not self.root:
            return 'An emptey tree'
        def traversal(node):
            nonlocal output 
            if node.left:
                traversal(node.left)
            if node.right:
                traversal(node.right)
            output += str(node.data)       
        traversal(self.root)
        return output


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print('value is present in tree.')

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True


        #                  23  

bst = BinarySearchTree()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(9))