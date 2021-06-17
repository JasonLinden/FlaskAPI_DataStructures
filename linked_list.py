class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_self(self):
        ll_string = ""
        node = self.head

        if node is None:
            print(None)

        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)

        if self.last_node is None:
            node = self.head
            while node.next_node:
                node = node.next_node

            node.next_node = Node(data, None)
            self.last_node = node.next_node
        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node

    def to_list(self):
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def get_user_by_id(self, user_id):
        node = self.head

        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None


# ll = LinkedList()

# ll.insert_beginning("1")
# ll.insert_beginning("2")
# ll.insert_beginning("3")
# ll.insert_beginning("4")
# ll.insert_beginning("5")
# ll.insert_beginning("6")
# ll.insert_beginning("7")
# ll.insert_beginning("8")

# ll.insert_at_end("end")
# ll.insert_at_end("end1")

# ll.print_self()

# print(ll.head.data)
# print(ll.last_node.data)
