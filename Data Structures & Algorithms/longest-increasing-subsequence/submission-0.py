class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        since we dont want to change the order we shouldn't need to sort them

        I'm getting hints that this is another decision tree problem.
        Either we memoize or try and build up to our max solution.

        We can process up to some array length and gradually introduce numbers.
        And the question we need to ask what do we need to do when we add a number to already increased sequence
        
        """
        res = []
        for num in nums:
            f,l = 0, len(res)
            while f < l:
                mid = (f+l) // 2
                if res[mid] < num:
                    f = mid+1
                else:
                    l = mid
            if f == len(res):
                res.append(num)
            else:
                res[f] = num
        return len(res)