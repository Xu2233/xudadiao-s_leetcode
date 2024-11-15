class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        打家劫舍，我看看怎么个事
        
        """

        ## 如果A开始
        dpforA = [0]*len(energyDrinkA)
        dpforA[0] = max (energyDrinkA[0])
        dpforA[1] = max ()

        