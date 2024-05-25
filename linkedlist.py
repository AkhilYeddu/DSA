class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_index(self, index, val):
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(val)
            return
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                raise IndexError("Index out of range")
            curr = curr.next
        if curr is None:
            raise IndexError("Index out of range")
        curr.next = ListNode(val, curr.next)
    
    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        prev = None
        curr = self.head
        for _ in range(index):
            if curr is None:
                raise IndexError("Index out of range")
            prev = curr
            curr = curr.next
        if curr is None:
            raise IndexError("Index out of range")
        prev.next = curr.next
    
    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def is_empty(self):
        return self.head is None
    
    def rotate(self, k):
        if self.head is None or self.head.next is None:
            return
        length = self.size()
        k = k % length
        if k == 0:
            return
        fast = self.head
        slow = self.head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = self.head
        self.head = slow.next
        slow.next = None
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    
    def append(self, val):
        if self.head is None:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
    
    def prepend(self, val):
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head
    
    def merge(self, other):
        if self.head is None:
            self.head = other.head
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = other.head
    
    def interleave(self, other):
        curr1 = self.head
        curr2 = other.head
        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2
        if curr2:
            curr1.next = curr2
    
    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val if slow else None
    
    def index_of(self, val):
        index = 0
        curr = self.head
        while curr:
            if curr.val == val:
                return index
            curr = curr.next
            index += 1
        return -1
    
    def split(self, index):
        if index < 0 or self.head is None:
            raise IndexError("Index out of range")
        if index == 0:
            other = LinkedList()
            other.head = self.head
            self.head = None
            return other
        prev = None
        curr = self.head
        for _ in range(index):
            if curr is None:
                raise IndexError("Index out of range")
            prev = curr
            curr = curr.next
        if curr is None:
            raise IndexError("Index out of range")
        other = LinkedList()
        other.head = curr
        prev.next = None
        return other