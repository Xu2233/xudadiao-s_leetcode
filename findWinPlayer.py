from collections import deque
class Solution(object):
    def findWinningPlayer(self, skills, k):
        """
        :type skills: List[int]
        :type k: int
        :rtype: int
        循环队列？
        什么脑筋急转弯？
        试一试双指针吧
        """
        tempdict = dict()
        for i in range(len(skills)):
            tempdict[i] = skills[i]

        # print(tempdict)
        left = 0
        right = 1
        









            
c = Solution()
print(c.findWinningPlayer([16,4,7,17], 562084119))