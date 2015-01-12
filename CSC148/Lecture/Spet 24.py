class EmptyStackError(Exception):
    """Exception used when calling pop on empty stack."""
    pass

class Stack:

    def __init__(self):
        """ (Stack) -> NoneType """
        self.items = []

    def is_empty(self):
        """ (Stack) -> bool """
        return len(self.items) == 0

    def push(self, item):
        """ (Stack, object) -> NoneType """
        # append adds an item to the END of a list
        self.items.append(item)

    def pop(self):
        """ (Stack) -> object """
        # calling the LIST metod pop, not the Stack method
        try:
            return self.items.pop()
        except IndexError:
            raise EmptyStackError


class Stack2:

    def __init__(self):
        """ (Stack) -> NoneType """
        self.items = []

    def is_empty(self):
        """ (Stack) -> bool """
        return len(self.items) == 0

    def push(self, item):
        """ (Stack, object) -> NoneType """
        self.items.insert(0, item)
        #self.items.reverse();self.items.append(item) reverse...

    def pop(self):
        """ (Stack) -> object """
        try:
            item = self.items[0]
            self.items = self.items[1:]
            return item
        except IndexError:
            raise EmptyStackError2

#==========================================================================
def compare_times():
    """Compare the times of operations of the two stacks."""
    stack = Stack()
    stack2 = Stack2()

    for i in range(1, 10):
        with Timer("Stack 1: push " + str(i*10000)):
            for j in range(10000):
                stack.push(j)
        with Timer("Stack 2: push " + str(i*10000)):
            for j in range(10000):
                stack2.push(j)

    for i in range(1, 10):
        with Timer("Stack 1: pop " + str(i*10000)):
            for j in range(10000):
                stack.pop()
        with Timer("Stack 2: pop " + str(i*10000)):
            for j in range(10000):
                stack2.pop()