class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value='null'):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            self.head= node
            self.head.next=current
    def includes(self,num):
        input=False
        current = self.head
        while current:
            if current.value == num:
                input=True
                break
            current=current.next
        return input
    def __str__(self):
        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += f"( {value} ) -> NULL"
                break
            output += f"( {value} ) -> "
            current=current.next
        return output

if __name__ == "__main__":
    class_input =LinkedList()
    class_input.insert(3)
    class_input.insert('and')
    class_input.insert(2)
    class_input.insert(1)
    actual = class_input.__str__()
    print(class_input.__str__())