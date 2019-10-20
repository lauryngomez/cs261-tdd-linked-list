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
            node.next = self.next
            self.next = node
            node.prev = self
            node.next.prev = node
        else:
            self = self.next
            self.append(node)

    def delete(self):
        left_node = self.prev
        right_node = self.next
        right_node.prev = left_node
        left_node.next = right_node

    def insert(self, node):
        left_node = self
        right_node = self.next
        node.prev = left_node
        node.next = right_node
        right_node.prev = node
        left_node.next = node

    def at(self, index):
        if index == 0:
            return self
        else:
            self = self.next
            return self.at(index-1)

    def search(self, value):
        # if self.value == value:
        #     return self
        # elif self.value != value:
        #     self = self.next
        #     return self.search(value)
        # else:
            return None

    def insert_in_order(self, node):
        self.append(node)