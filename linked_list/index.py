from linked_list import LinkedList
from node import Node

# code execution
if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.insert_at_pos('wes', 1)

    llist.traverse()