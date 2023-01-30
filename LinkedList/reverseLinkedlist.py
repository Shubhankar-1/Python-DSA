from linkedList import LinkedList

lis = LinkedList([1,2,3,4,5,6])

lis.print()
def reverseLinkedList(head):

    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    lis.head = prev
    lis.print()

reverseLinkedList(lis.head)

