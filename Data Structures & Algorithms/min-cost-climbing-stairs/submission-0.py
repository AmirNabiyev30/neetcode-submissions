class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #top down
        """
        Each position of the array will represent the cost to reach the last position of the array
        """
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        return min(cost[0],cost[1]) 


        