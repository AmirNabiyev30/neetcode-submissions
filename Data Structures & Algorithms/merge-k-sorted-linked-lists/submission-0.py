# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #so im thinking we iterate through each node comparing values to minimum
        #value that've seen.
        #With this minimum value that we have seen before we link it to a node and
        #so even an empty list of lists is falsy

        """
        My logic is that I want to iterate through every linked list compare the val to a minium
        and then link that list while also moving that list along 
        the while will finish when every list meets a null pointer
        """
        dummy  = ListNode()
        #we want this loop to run until lists is filled with NULL values
        curr = dummy
        while True:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[i].val < lists[minNode].val:
                    minNode = i
            if minNode == -1:
                break #all the lists are none so we never found a value
            
            curr.next = lists[minNode] 
            lists[minNode] = lists[minNode].next
            curr = curr.next
        return dummy.next

        