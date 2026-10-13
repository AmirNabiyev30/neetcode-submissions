class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        this problem will definitely require a dfs approach i believe

        at each point is a decision tree, the problem is that sequence must
        be retained

        decision tree

        if we include a number we need to include numbers only next to it,
        we could possibly memoize based on future decisions, 

        would it better to do bottom up approach. 
        if we have a maximum sub array how would we change our solution if we added a number,
        
        if it increases our total we keep it, if it decreases our total we disregard is the simple idea,

        we need to keep a running sum, or have the decision tree and        memoize
        we need to keep a running sum cause we will never know  


        """
        res = max(nums)
        curmin,curmax = 1 ,1

        for n in nums:
            if n == 0:
                curmin,curmax = 1,1
            tmp = curmax * n
            curmax = max(tmp,n*curmin,n)
            curmin = min(tmp,n*curmin,n)
            res = max(res,curmax)
        return res
        