class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #now the pointer approach

        slow,fast = 0,0
        #advance the pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        #now the pointers intersected
        #create our second pointer and implement floyds algorithmn

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

