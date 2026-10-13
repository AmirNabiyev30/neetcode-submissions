class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #lets solve this problem 
        #so first we create the linked list based off the nodes and their positions

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1
        