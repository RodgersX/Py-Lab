from node import Node

class LinkedList:
    def __init__(self):
        self.head = None  # empty list

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def insert_first(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def insert_last(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = temp

    def insert_at_pos(self, data, pos):
        count = 1
        curr = self.head

        while count < pos-1 and curr is not None:
            curr = curr.next
            count += 1
        temp = Node(data)
        temp.next = curr.next
        curr.next = temp

    def traverse(self):
        curr = self.head

        while curr is not None:
            print(curr.data)
            curr = curr.next

    def del_from_first(self):
        try:
            if self.head is None:
                raise Exception('List is Empty!')

            temp = self.head
            self.head = self.head.next
            del temp
        except Exception as e:
            print(str(e))

    def del_from_end(self):
        try:
            if self.head is None:
                raise Exception('List is Empty')

            curr = self.head
            prev = None
            while curr is not None:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            del curr

        except Exception as e:
            print(str(e))

    def del_at_pos(self, pos):
        try:
            if self.head is None:
                raise Exception('List is Empty')

            curr = self.head
            prev = None
            count = 1

            while curr is not None and count < pos:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next
            del curr
        except Exception as e:
            print(str(e))

