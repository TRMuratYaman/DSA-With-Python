from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in place and returns the sorted linked list
    """
    if linked_list.head == None or linked_list.size() == 1:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Splits a linked list into two halves:left_half and right_half.
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        mid = size // 2
        # returns middle node of the linked list.
        middle_node = linked_list.middle_node_at_index(mid - 1)
        # we split the linked list to left linked list and right linked list.
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = middle_node.next_node
        middle_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges a sorted linked list and returns it.
    """
    # creating new empty linked list so we can add nodes from left and right linked lists to named merged linked list in ascending order.
    merged = LinkedList()
    # creating fake
    merged.add(0)
    # set current to the head of the linked list.
    current = merged.head

    left_head = left.head
    right_head = right.head
    # iterate over left and right sub linked lists until we reach the tail node.
    while left_head or right_head:
        # if head node of right is none,we're past the tail.
        # add the node from left to merged linked list.
        if right_head == None:
            current.next_node = left_head
            left_head = left_head.next_node
        # if head node of left is none,we're past the tail.
        # add the node from right to merged linked list.
        elif left_head == None:
            current.next_node = right_head
            right_head = right_head.next_node
        # if both linked lists are not none,we comperase the datas which is greater.
        else:
            left_data = left_head.data
            right_data = right_head.data
            # if left linked list's data is smaller than right linked list's data,we add left data to merged linked list.
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # if left linked list's data is greater than right linked list's data,we add right data to merged linked list.
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node
    # we drop the fake node from sorted new merged linked list.
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(30)
l.add(25)
l.add(40)
l.add(15)
l.add(100)
l.add(60)
l.add(70)
l.add(35)
print(l)
sorted = merge_sort(l)
print(sorted)
