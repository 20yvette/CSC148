# Lab 3 - Queues
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------


class EmptyQueueError(Exception):
    """Error raised when trying to dequeue from an empty queue."""
    pass


class Queue:
    """Queue class.
    A class implementing the Queue ADT, using a list.

    Attributes:
    - ???
    """

    def __init__(self):
        """ (Queue) -> NoneType
        Create an empty queue.
        """
        self.items = []

    def is_empty(self):
        """ (Queue) -> bool
        Return True if the queue is empty.
        """
        return self.items == []

    def enqueue(self, item):
        """ (Queue, object) -> NoneType
        Add item to the back of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """ (Queue) -> object
        Remove and return the front item, if there is one.
        Raise EmptyQueueError if the list is empty.
        """
        if self.items[0] == None:
            raise EmptyQueueError
        else:
            self.items.pop(0)


def product(queue):
    """ (Queue of number) -> number

    Return the product of all numbers in queue.
    Return 1 if queue is empty.
    You may change queue (and in particular, remove all its items).

    Although as a bonus, try *not* changing the queue!
    """
    if queue.is_empty():
        return 1
    else:
        tempQ = []
        product = 1
        tempVar = 0
        while not queue.is_empty():
            tempVar = queue.pop()
            product = product * tempVar
            tempQ.append(tempVar)
        for i in tempQ:
            queue.enqueue(i)
        return product
if __name__=="__main__":
    q=Queue()
    q.enqueue(1)
    print(q.queue)