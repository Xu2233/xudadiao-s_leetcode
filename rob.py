class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        经典DP问题，如果i不偷，则获得dp[i-1]
        如果i偷，则获得dp[i-2]+nums[i]
        取两者最大值
        """
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]= max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
        

c = Solution()
print(c.rob([1,2,3,1]))


       
        