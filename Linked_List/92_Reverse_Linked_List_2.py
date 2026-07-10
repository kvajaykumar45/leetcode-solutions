class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # 1. Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next
        
        # Now prev is the (left-1)th node
        curr = prev.next  # curr is the left-th node
        
        # 2. Reverse the sublist
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next
