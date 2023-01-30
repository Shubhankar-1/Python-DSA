class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        try:
            slow = head
            fast = head.next
            print(slow)
            print(fast)
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

                
        # if pos < len(head):
        #     return True

        # return False


if __name__ == "__main__":
    s = Solution()
    result = s.hasCycle(head=[3, 2, 0, -4])
    print(result)
