class EmptyValue:
    pass

class Tree:
    def __init__(self, root=EmptyValue):
        self.root = root
        self.subtrees = []
        
    def is_empty(self):
        return self.root is EmptyValue

#non-mutating

    def size(self):
        if self.is_empty():
            return 0 
        else:
            size = 1
            for subtree in subtrees:
                size += subtree.size()
            return size
        
    def count_leaves(self):
        if self.is_empty():
            return 0
        elif self.subtrees == []:
            return 1
        else:
            count = 0
            for subtree in self.subtrees:
                count += subtree.count_leaves()
            return count 
    
    def internal_nodes(self):
        if self.is_empty():
            return 0
        elif self.subtrees == []:
            return 0
        else:
            count = 1
            for subtree in self.subtrees:
                count += subtree.internal_nodes()
            return count
    
    def count_d(self,d):
        if self.is_empty():
            return 0
        elif d ==1:
            return 1
        else:
            count = 0
            for subtree in self.subtrees:
                count += subtree.count_d(d-1)
            return count 
    
    def count_less(self, d):
        if self.is_empty():
            return 0
        elif d == 1:
            return 1
        else:
            count = 1
            for subtree in self.subtrees:
                count += subtree.count_less(d-1)
            return count 
        
            
    def count_more(tree, d):
        if tree.is_empty():
            return 0
        else:
            if d == 1:
                count = 1
                for subtree in tree.subtrees:
                    count += subtree.count_more(1)
                return count
            else:
                count = 0
                for subtree in tree.subtrees:
                    count += subtree.count_more(d-1)                
                return count 
            
    def check_item(self, item):
        if self.is_empty():
            return 0
        else:
            if self.root == item:
                count = 1
                for subtree in self.subtrees:
                    count += subtree.check_item(item)
                return count
            else:
                count = 0
                for subtree in self.subtrees:
                    count += subtree.check_item(item)
                return count                    
    
    def sum(self):
        if self.is_empty():
            return 0
        else:
            sum = self.root
            for subtree in self.subtrees:
                sum += subtree.sum()
            return sum
        
    def repeat_helper(self,seen): 
        if self.is_empty():
            return False
        elif self.root in seen:
            return True
        else:
            seen.append(self.root)
            for subtree in self.subtrees:
                if self.repeat_helper(seen):
                    return True
            return False
    
    def repeat(self):
        return self.repeat_helper([])
        
        
    
    #def count_repeated(self):
        
        
    def count_even(self):
        if self.is_empty():
            return 0
        
            
            
class LLNode(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

def last_node(start_node):
    new = LLNode()
    curr = start_node.value
    while not curr.next is None:
        new.value = curr
        curr = curr.next.value
    return curr

            