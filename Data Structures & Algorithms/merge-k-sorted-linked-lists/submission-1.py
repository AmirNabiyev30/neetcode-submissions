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
        if not lists or len(lists) == 0:
            return None
        #now we do the o(nlogk) method
        #we want to continously merge the lists until we reach lists of length 1 
        while len(lists) > 1:
            #we want to iterate every 2
            mergedlists = []

            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                combined = self.merge2Lists(l1,l2)
                mergedlists.append(combined)
            lists = mergedlists
        return lists[0]
    def merge2Lists(self,l1,l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next



        