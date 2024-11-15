class Solution:
    def sumDigitDifferences(self, nums):
        s = str(nums[0])
        L = len(s)
        n = len(nums)
        ans = 0
        for i in range(L):
            mp = {}
            for x in nums:
                zhi = str(x)
                if zhi[i] in mp:
                    mp[zhi[i]] += 1
                else:
                    mp[zhi[i]] = 1
            val = n
            for x, y in mp.items():
                ans += y * (val - y)
                val -= y
        return ans




c=Solution()
c.sumDigitDifferences([100,123,321])