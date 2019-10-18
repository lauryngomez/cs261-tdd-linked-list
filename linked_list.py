# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Lauryn Gomez

class LinkedList:

    def __init__(self, value = None):
        self.value = value
        self.next = self
        self.prev = self

    def is_sentinel(self, value = None):
        if self.value == value:
            return True
        else:
            return False

    def is_empty(self, value = None):
        if self.next == self and self.prev == self:
            return True
        else:
            return False
    
    def is_last(self, value = None):
        return self.next.is_sentinel()

    def last(self, value = None):
        if self.next.is_sentinel():
            return self
        else:
            self = self.next
            return self.last()
    
    def append(self, node):
        if self.is_empty(): 
            self.next = node
            node.next = self
            node.prev = self
            self.prev = node
        elif self.is_last():
            self.next = node
            node.next = self.next
            node.prev = self
            node.next.prev = node
        else:
            self = self.next.append(node)