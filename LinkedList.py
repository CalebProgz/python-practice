class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index cannot be negative")
            return
        new_node = Node(data)
        if index == 0:
            self.insert_at_start(data)
            return
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                print("Index out of range")
                return
            curr = curr.next
        if curr is None:
            print("Index out of range")
            return
        new_node.next = curr.next
        curr.next = new_node

    def delete_at_index(self, index):
        if index < 0:
            print("Index cannot be negative")
            return
        if self.head is None:
            print("List is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(index - 1):
            if curr is None or curr.next is None:
                print("Index out of range")
                return
            curr = curr.next
        if curr.next is None:
            print("Index out of range")
            return
        curr.next = curr.next.next

    def search(self, value):
        curr = self.head
        index = 0
        while curr:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return -1

    def display(self):
        curr = self.head
        if not curr:
            print("List is empty")
            return
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
