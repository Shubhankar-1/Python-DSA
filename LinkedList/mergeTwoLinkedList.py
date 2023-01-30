class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Linked:
#     def __init__(self):
#         self.head = None

#     def insert(self, val):
#         if self.head is None:
#             self.head = ListNode(val, None)
#             return

#         itr = self.head
#         while itr.next:
#             itr = itr.next

#         itr.next = ListNode(val, None)

#     def show(self):
#         if self.head is None:
#             print("Empty")
#             return

#         itr = self.head

#         lis=[]
#         while itr:
#             lis.append(itr.val)
#             itr = itr.next

#         print(lis)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            curr = dummy = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    curr = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    curr = list2
                    list2 = list2.next

            if list1 or list2:
                curr.next = list1 if list1 else list2

            return dummy.next


if __name__ == "__main__":
    s = Solution()
    result = s.mergeTwoLists(l1=[1, 2, 4], l2=[1, 3, 4])
    print(result)
