def countNodes(head):
    nodes = 1
    current = head

    while head.next is not None:
        # need to set current to the next node to keep movign through the list
        current = current.next
        nodes += 1

    return nodes


# find how many nodes there are in the linked list
# Go all the way to end until the next attribute is null (that means it's the end)
#
