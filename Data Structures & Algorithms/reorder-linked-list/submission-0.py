# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #can be done with 2 pointers
        slow,fast = head,head
        while fast is not None and fast.next is not None:
            #move the fast pointer along
            fast = fast.next.next
            slow = slow.next
        #slow is the middle of the linked list    
        
        #reverse the second half
        #we need another 2 pointers
        #one pointer to keep where we are going 
        #one pointer to reverse connections
        
        second = slow.next
        prev = slow.next = None
        while second is not None:
            #save connection
            nxt = second.next
            #reverse conncetion
            second.next = prev
            #iteration
            prev = second
            second = nxt
        
        #prev is the head of the reverse linked list

        #now we start merging the lists
        #we will pair head and prev and continously iterate through them
        first,second = head,prev

        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1 #squishing second in between the 2 nodes
            first,second = tmp1,tmp2
