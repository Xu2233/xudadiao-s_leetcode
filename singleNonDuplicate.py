class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
        请你找出并返回只出现一次的那个数。
        你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。
        """
        #遍历奇数法
        if len(nums) ==1:
            return nums[-1]
        cnt = 0
        for i in range(int((len(nums)-3)/2)+1):
            if nums[i*2] != nums[i*2+1]:
                return nums[i*2]

        return nums[-1]
        
        #二分法
        

c = Solution()
print(c.singleNonDuplicate([3,3,7,7,10,11,11]))
        