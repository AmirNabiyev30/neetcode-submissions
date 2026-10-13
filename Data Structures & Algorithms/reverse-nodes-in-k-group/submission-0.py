# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
    
        """
        def reverse(start, end):
            prev = None
            curr = start
            stop = end.next  # store this once before the loop
            while curr != stop:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt


        dummy = ListNode(next = head)
        start = head
        end = dummy
        prev_start = dummy 
        while True:
            for i in range(k):
                if end == None: #we reached the end
                    return dummy.next
                end = end.next # traverse 
            if end == None:
                return dummy.next
            next_group = end.next # saving next connection

            reverse(start,end)

            #stich together
            prev_start.next = end
            start.next = next_group

            #advance
            prev_start = start
            end = prev_start
            start = next_group
        
        return dummy.next
        