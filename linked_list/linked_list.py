class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(head:Node):
    node = head
    while node:
        print(node.data)
        node = node.next

def traverse(head:Node):
    pass

if __name__ == "__main__":
    head = Node(1)
    node_1 = Node(2)
    node_2 = Node(3)
    head.next = node_1
    node_1.next = node_2

    print_linked_list(head)