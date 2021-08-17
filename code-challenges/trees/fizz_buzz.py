class Node:
    def __init__(self, value):
        self.value = value
        self.result=[]

class k_Ary:
    def __init__(self):
        self.root = None


def fizz_buzz_tree(k_Ary):
    def traverse(node):
        if node.result:
            for i in range(len(node.result)):
                traverse(node.result[i])
                if node.result[i].value %5 == 0 and node.result[i].value %3 == 0:             
                    node.result[i].value='Fizz Buzz'
                elif node.result[i].value %3 == 0:
                    node.result[i].value='Fizz'     
                elif node.result[i].value %5 == 0:
                    node.result[i].value='Buzz'
                else:
                    node.result[i].value=str(node.result[i].value)
    traverse(k_Ary.root)
    if k_Ary.root.value  %5 == 0 and k_Ary.root.value %3 == 0:                
        k_Ary.root.value='Fizz Buzz'
    elif k_Ary.root.value %5 == 0:
        k_Ary.root.value='Buzz'
    elif k_Ary.root.value %3 == 0:
        k_Ary.root.value='Fizz'     
    else:
        k_Ary.root.value=str(k_Ary.root.value)

    return k_Ary
