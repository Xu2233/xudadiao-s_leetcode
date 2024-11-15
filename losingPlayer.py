class Solution(object):
    def losingPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        只有一种组成方式 75+10*4
        
        """
        winner = 1
        while x>=0 and y>=0:
            x = x-1
            y = y-4
            winner = -winner
        if winner > 0:
            return "Alice"
        else:
            return "Bob"


            

c = Solution()
print(c.losingPlayer(1,4))


        