class Solution:
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        这个思路嘛就逮滴很
        
        这题的思路就是
        遍历数组
        然后如果当前数字和前一个数字差1
        则计数+1
        如果计数大于k
        则输出
        否则计数为1
        继续遍历
        直到遍历完数组
        直接给时间复杂度干到O(n)

        """

        n = len(nums)
        cnt = 0
        ans = [-1]*(n-k+1)
        for i in range(n):
            if i == 0 or nums[i]-nums[i-1]!=1:
                cnt =1
            else:
                cnt +=1

            if cnt >=k:
                ans[i-k+1] = nums[i]
        return ans



    
c= Solution()
nums= [1,2,3,4,3,2,5]
print(c.resultsArray(nums,3))
                    
            
                    
                




        
    
        