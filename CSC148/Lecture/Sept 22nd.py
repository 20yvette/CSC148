from stack import Stack

def size(stack):
    count = 0
    while not stack.is_empty:
        stack.pop()
        count += 1
    retuen count 
    
def size2(stack):
    temp_stack = Stack ()
    count = 0
    while not stack.is_empty:
        x = stack.pop()
        temp_stack.push(x)
        count += 1
    while not temp_stack.is_empty:
        x = temp_stack.pop()
        stack.push(x)
    return count