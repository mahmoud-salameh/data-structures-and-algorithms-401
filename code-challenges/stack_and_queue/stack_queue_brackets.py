
from stack_and_queue.stack_and_queue import*

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




