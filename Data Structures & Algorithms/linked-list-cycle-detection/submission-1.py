# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #we want to at least be spaec o(n) and 0(1) mem
        #to maintain an o(1) mem we can maintain a growing list of previous states
        #we want to return the index of that cycle
        #im thinking we can change the val of the node and include the index
        #and once we loop back if we see and negative change in index value,we return that index
        #otherwise return -1
        if head == None:
            return False
        p1 = head
        nxt = head.next
        index = 0
        while p1:
            #if we ever reach the end of the list
            if nxt == None:
                return False
            #this isnt the end of the list of there is a cycle
            #add an index element to the nodes to keep track of index
            p1.val = [p1.val,index]
            #if the nxt points to something that has a 2nd element, we know we there is a cycle
            if isinstance(nxt.val,list):
                return True
            p1 = nxt
            nxt = p1.next
        


            
        