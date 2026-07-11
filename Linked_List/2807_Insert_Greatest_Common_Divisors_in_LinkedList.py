# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = head
        current2 = head.next

        while current2:
            g = math.gcd(current1.val, current2.val)
            newnode = ListNode(g)
            newnode.next = current1.next
            current1.next = newnode
            current1 = newnode.next
            current2 = current2.next
        return head
