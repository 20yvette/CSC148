class EmptyValue:
    """Dummy class used to represent the "first" item
    of an empty list.

    This is created so that we can make linked lists
    that contain None.
    """
    pass

class LinkedListRec:
    """Linked List with a recursive implementation.
    Note that there is no "Node" class with this implementation.

    Attributes:
    - first (object): the first item stored in this list,
                      or EmptyValue if this list is empty
    - rest (LinkedListRec): a list containing the other items
                            in this list, or None if this list is empty
    """

    def __init__(self, items):
        """ (LinkedListRec, list) -> NoneType

        Create a new linked list containing the elements in items.
        If items is empty, self.first initialized to EmptyValue.
        """
        if len(items) == 0:
            self.first = EmptyValue
            self.rest = None
        else:
            self.first = items[0]
            self.rest = LinkedListRec(items[1:])
            
    def is_empty(self):
        return self.first is EmptyValue
    
# Non-mutating

    def size(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.rest.size()

    def find_6(self):
        if self.is_empty():
            return 0
        else:
            if self.first == 6:
                return 1 + self.rest.find_6()
            else:
                return self.rest.find_6()
            
    def find_item(self,item):
        if self.is_empty():
            return 0
        else:
            if self.first == item:
                return 1 + self.rest.find_item()
            else:
                return self.rest.find_item()
            
    def find_sum(self):
        if self.is_empty():
            return 0
        else:
            return self.first + self.rest.find_sum()
        
    def find_repeated(self):
        if self.is_empty():
            return False
        else:
            curr = self.rest
            while not curr.is_empty():
                if self.first == curr.first:
                    return True
                curr = curr.rest
            return self.rest.find_repeated()
        
    def count_even(self):
        if self.is_empty():
            return 0
        else:
            if self.first % 2 == 0:
                return 1 + self.rest.count_even()
            else:
                return self.rest.count_even()
    
    def return_duplicate(self):
        if self.is_empty():
            return []
        else:
            curr = self.rest
            lst = []
            while not curr.is_empty():
                if self.first == curr.first:
                    lst.append(self.first)
                curr = curr.rest
            new = self.rest.return_duplicate()
            lst = lst+new
            return lst
            
    def return_number(L1, L2):
        if L1.is_empty() or L2.is_empty():
            return 0
        else:
            while L1.rest.is_empty():
                if L1.first == L2.first:
                    return 1 + L1.return_number(L2.rest)
                else:
                    return L1.return_number(L2.rest)
        
        return LinkedListRec([L1.first]).return_number(L2) + L1.rest.return_number(L2)
            
    def merge(L1,L2):
        if L1.is_empty() and L2.is_empty():
            return LinkedListRec([])
        elif L1.is_empty():
            merged = LinkedListRec([L2.first])
            merged.rest = L2.rest
            return merged
        elif L2.is_empty():
            merged = LinkedListRec([L1.first])
            merged.rest = L1.rest
            return merged            
        elif L1.first <= L2.first:
            merged = LinkedListRec([L1.first])
            merged.rest = merge(L1.rest, L2)
            return merged
        else:
            merged = LinkedListRec([L2.first])
            merged.rest = merge(L1, L2.rest)            
            return merged
            
        
#Mutating
    
    def remove_first(self):
        if self.is_empty():
            raise IndexError
        else:
            self.first = self.rest.first
            self.rest = self.rest.rest
    
    def remove_ith(self, i):
        if self.is_empty():
            raise IndexError
        elif i >= len(self):
            raise IndexError
        elif i == 0:
            self.remove_first()
        else:
            self.rest.remove(i-1)

    def remove_even(self):
        if self.is_empty():
            raise Error
        else:
            if self.first % 2 == 0:
                self.remove_first()
            else:
                self.rest.remove_even()
                
    def insert_front(self,item):
        temp = LinkedListRec([])
        temp.first = self.first
        temp.rest = self.rest
        self.first = item
        self.rest = temp
            
    def insert_back(self,item):
        if self.is_empty():
            self.first = item
            self.rest = LinkedListRec([])
        elif len(self) == 1:
            self.first = self.first
            self.rest = LinkedListRec([item])
        else:
            self.rest.insert_back(item)

    def insert(self, item, i):
        if i >= len(self):
            raise IndexError
        elif i == 0:
            self.insert_first()
        else:
            self.rest.insert(item, i-1)
    
    def remove_dup(self):
        if self.is_empty():
            pass
        else:
            curr = self.rest
            while not curr.is_empty():
                if self.first == curr.first:
                    self.remove_first()
                curr = curr.rest
            self.rest.remove_dup()
            
    def contatenate(L1,L2):
        if L1.is_empty():
            L1.first = L2.first
            L1.rest = L2.rest
        else:
            contatenate(L1.rest, L2)
            
    def remove_firstn(self, n):
        if self.is_empty():
            pass
        elif n == 0:
            pass
        elif n == 1:
            self.remove_first()
        else:
            self.rest.remove_firstn(n-1)    
      
    def remove_lastn(self,n):
        if self.is_empty():
            pass
        elif n==0:
            pass
        else:
            curr = self.rest
            while not curr.rest.is_empty():
                curr = curr.rest
            curr.first = EmptyValue
            self.remove_lastn(n-1)
        
    def remove_all(self):
        if self.is_empty():
            pass
        elif self.first == 1:
            self.first = self.first
            self.rest = LinkedListRec([])
        else:
            self.rest.remove_all()
        
        
                
            
               
        
        
        
        
        