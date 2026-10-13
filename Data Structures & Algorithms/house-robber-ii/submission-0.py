class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0],self.hb1(nums[1:]),self.hb1(nums[:-1]))
    
    def hb1(self,nums):
        rb1,rb2 = 0,0
        for num in nums:
            new_rob = max(rb1+num,rb2)
            rb1 = rb2
            rb2 = new_rob
        return rb2