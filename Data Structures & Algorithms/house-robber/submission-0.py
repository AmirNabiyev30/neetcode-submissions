class Solution:
    def rob(self, nums: List[int]) -> int:
        #we can have another array that shows both paths
        if len(nums) == 1:
            return nums[0]
        #modify in place
        rob1,rob2 = 0,0
        for n in nums:
            tmp = max(n+rob1,rob2)
            rob1  = rob2
            rob2 = tmp
        return rob2