
class Node:
    """
    We are creating new nodes using this class.
    """
    data = None
    next_node = None

    def __init__(self, data):
        """
        We are adding data into our node while we are creating node.
        """
        self.data = data

    def __repr__(self):
        """
        When we use the print build-in function,this method returns a string value.
        """
        return "Data : %s" % self.data



class LinkedList:
    def __init__(self):
        """
        We are creating an empty linked list at the start.
        """
        self.head = None

    def is_empty(self):
        """
        This method checks is our linked list has nodes or not.
        """
        return self.head == None

    def size(self):
        """
        This method calculates the number of the nodes in the Linked List.
        """
        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        This method adds a new node head of the Linked List.
        """
        new = Node(data)
        new.next_node = self.head
        self.head = new

    def search(self, key):
        """
        This method checks is there any data in the linked list we search of.
        """
        current = self.head

        while current != None:
            if current.data == key:
                return True
            else:
                current = current.next_node
        return False


    def insert(self, data, index):
        """
        This method inserts a node to random position in the linked list.
        """
        if index == 0:
            self.add(data)
        elif index > 1:
            new_node = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = prev_node.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node


    def middle_node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current


    def remove(self, key):
        """
        This method removes the node in the linked list.
        """
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

    def __repr__(self):
        """
        This method shows the linked list on the console.
        """
        nodes = []
        current = self.head

        while current != None:
            if current == self.head:
                nodes.append("[Head : %s]" % current.data)
            elif current.next_node == None:
                nodes.append("[Tail : %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return "->".join(nodes)

def LinkedList_Operations():
    print("Creating Linked List")
    l = LinkedList()
    print("Is Linked List Empty ? :", l.is_empty())
    print("Adding nodes at Linked List")
    l.add(10)
    l.add(20)
    l.add(30)
    l.add(40)
    l.add(50)
    print("Show The new Linked List :", l)
    print("How Many Nodes In The Linked List ? :", l.size())
    print("Is the data 30 In the Linked List :", l.search(30))
    l.insert(35 ,3)
    print(l)
    l.remove(10)
    print(l)
    print("Is the data 60 In the Linked List :", l.search(60))





