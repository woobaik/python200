class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None
        print(f"{self}", 'Self value')


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head

        self.head = new_node

    def print_list(self):

        if self.head == None:
            print('No Node here, please enter with insert Head')
            return 
        
        
        current = self.head
        while current:
            print(current.value, end="=>")
            current = current.next



list = LinkedList()
list.insert_head('head1')
list.insert_head('head2')

list.print_list()
