class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        my_dict = {i:0 for i in range(prizePositions[-1])}

        for i in prizePositions:
            my_dict[i-1] += 1

        print(my_dict)    




c=Solution()
c.maximizeWin([1,1,2,2,3,3,5],2)