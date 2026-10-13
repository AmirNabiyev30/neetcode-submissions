# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we can do a fast and slow pointer approach, the fast pointer will approach to the end of the list
        #instead of needing the counter
        #we can allow n to be the fixed size of the distance between the pointers
        #the fast pointer will go to the end of the list of a seperation of size n
        #from the slow pointer
        #so the slow pointer will be on the node before the node we need to remove
        dummy = ListNode(next = head)
        nth = dummy
        fast = head
        #create the needed distance between the 2 pointers
        while n > 0:
            fast = fast.next
            n-=1
        while fast:
            fast = fast.next
            nth = nth.next
        
        nth.next = nth.next.next
        return dummy.next
        
        

            


        

        