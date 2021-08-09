from stack_and_queue.stack_and_queue import *
import pytest


def test_push(stack_input):
    actual = stack_input.top.value
    expected = "N"
    assert actual == expected

def test_pop(stack_input):
    actual = stack_input.pop()
    expected = "N"
    assert actual == expected
    assert stack_input.top.value == 9

def test_is_empty_true(stack_input):
    stack_input.pop()
    stack_input.pop()
    stack_input.pop()
    assert stack_input.isEmpty() == True

def test_peek_stack(stack_input):
    actual = stack_input.peek()
    expected = "N"
    assert actual == expected
    assert stack_input.top.value == "N"

def test_is_empty_stack(stack_input):
    assert stack_input.isEmpty() == False

def test_stack_exception(stack_input):
    stack_input.pop()
    stack_input.pop()
    stack_input.pop()
    assert stack_input.pop()=="An empty stack"
    assert stack_input.peek()=="An empty stack"

@pytest.fixture
def stack_input():
    stack = Stack()
    stack.push(-4)
    stack.push(9)
    stack.push("N")
    return stack

""" ------------------------------------------------------------------------------------------------------ """

# def test_enqueue(queue_input):
#     assert queue_input.rear.value == 7
#     assert queue_input.front.value == 9

# def test_dequeue(queue_input):
#     data = queue_input.dequeue()
#     assert data == 9
#     assert queue_input.front.value == "Mahmoud"

# def test_peek_queue(queue_input):
#     assert queue_input.peek()==9

# def test_is_empty_true(queue_input):
#     data = queue_input.dequeue()
#     data = queue_input.dequeue()
#     data = queue_input.dequeue()
#     data = queue_input.dequeue()
#     assert queue_input.isEmpty()==True

# def test_queue_exception(queue_input):
#     queue_input.dequeue()
#     queue_input.dequeue()
#     queue_input.dequeue()
#     queue_input.dequeue()
#     assert queue_input.dequeue()=="An empty Queue"
#     assert queue_input.peek()=="An empty Queue"

# def test_is_empty_Queue(queue_input):
#     assert queue_input.isEmpty()==False

# @pytest.fixture
# def queue_input():
#     queue = Queue()
#     queue.enqueue(9)
#     queue.enqueue("Mahmoud")
#     queue.enqueue(-4)
#     queue.enqueue(7)
#     return queue




""" ---------------------------------------------stack-queue-pseudo tests---------------------------------------------------- """


def test_enqueue_Expected_failure(queue_vals):
    actual = queue_vals.__str__()
    expected = '( 9 ) -> ( mahmoud ) -> ( -4 )'
    assert actual != expected

def test_enqueue_edge_case():
    queue = PseudoQueue()
    actual = queue.enqueue()
    expected = 'Please put a value'
    assert actual == expected


def test_dequeue_Expected_failure(queue_vals):
    dequeue_value=queue_vals.dequeue()
    actual = queue_vals.__str__()
    expected = '( 9 ) -> ( mahmoud ) -> ( -4 ) -> ( 7 )'
    assert actual != expected
    assert dequeue_value != -4

def test_dequeue_edge_case():
    queue = PseudoQueue()
    actual = queue.dequeue()
    expected = 'The Queue is empty'
    assert actual == expected


@pytest.fixture
def queue_vals():
    queue = PseudoQueue()
    queue.enqueue(7)
    queue.enqueue(-4)
    queue.enqueue("mahmoud")
    queue.enqueue(9)
    return queue

""" ---------------------------------------------stack-queue-animal-shelter-tests---------------------------------------------------- """

def test_return_cat_name(que_val):
    actual = que_val.dequeue('cat')
    expected = 'nimnim'
    assert actual == expected

def test_Expected_failure_return_wrong_dog_name(que_val):
    actual = que_val.dequeue('dog')
    expected = 'bimbus'
    assert actual != expected

def test_Not_Cat_Or_Dog_return_None(que_val):
    actual = que_val.dequeue('empty')
    expected = None
    assert actual == expected


@pytest.fixture
def que_val():
    dj = Dog('toast')
    mika = Dog('mika')
    bimbus = Dog('bimbus')
    nimnim = Cat('nimnim')
    mimi = Cat('mimi')
    mshmsh = Cat('mshmsh')
    animal_shelter = Animal_shelter()
    animal_shelter.enqueue(dj)
    animal_shelter.enqueue(mika)
    animal_shelter.enqueue(bimbus)
    animal_shelter.enqueue(nimnim)
    animal_shelter.enqueue(mimi)
    animal_shelter.enqueue(mshmsh)
    return animal_shelter
















