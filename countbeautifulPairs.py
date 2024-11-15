class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        前面的第一个，后面的最后一个，最大公约数为1
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                nums1 = int(str(nums[i])[0])
                nums2 = int(str(nums[j])[-1])

                if self.gcd(nums1,nums2)==1:
                    count +=1
        return count

                    
    
    def gcd(self, a, b):
        while b!= 0:
            a,b =b,a%b
            
        return a

c = Solution()
print(c.countBeautifulPairs([31,25,72,79,74]))

            

        