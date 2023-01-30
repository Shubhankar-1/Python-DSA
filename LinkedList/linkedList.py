class ListNode:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,arr):
        self.head = curr = ListNode()

        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next
        
        self.head = self.head.next

    def print(self,head = None):
        curr = head if head else self.head
        while curr != None:
            print(curr.data,end="")
            curr = curr.next

        print("")

