from structures import LinkedListNode, LinkedList

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    
    def prnt(self):
        results = []
        node = self.head
        while node:
            results.append(node.val)
            node = node.next
        print(results)

    def insert(self, val):
        node = LinkedListNode(val)
        node.next = self.head
        self.head = node
    
    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def search(self, val):
        node = self.head
        while node:
            if node.val == val:
                return True
            node = node.next
        return False
    
    def index_search(self, idx):
        count = 0
        node = self.head
        while node:
            if count == idx:
                return node.val
            count += 1
            node = node.next
    
    def index_replace(self, idx, new_val):
        index = 0
        node = self.head
        while not index == idx:
            index += 1
            node = node.next
        node.val = new_val

        
            


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.prnt()
print("size" ,ll.size())
print('Search',ll.search(4))
print('Search',ll.search(12))
print('index search 4 =', ll.index_search(4))
print('index search 1 =', ll.index_search(1))
ll.index_replace(2, 12)
ll.prnt()