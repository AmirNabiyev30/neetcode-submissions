class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(curr_sum,start,path):
            if curr_sum > target: #prune this path
                return False
            if curr_sum == target: # exactly what we wanted
                return True
            for i in range(start,len(nums)):
                path.append(nums[i])
                result = dfs(curr_sum+nums[i],i,path)
                if result == True:
                    self.res.append(list(path))
                path.pop()
                

        dfs(0,0,[])
        return self.res