class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        n是总长度
        给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。
        每次切割的成本都是当前要切割的棍子的长度
        递归要点：
        递归边界、递归入口、递归公式

        """
        #成本
        cuts.sort()
        cuts = [0] + cuts + [n]
        def dfs(i, j):
            # 递归边界 无法切割
            if i + 1 == j:
                return 0
            ans = float('inf')

            # 递归入口
            for k in range(i + 1, j):
                ans = min(ans, dfs(i, k) + dfs(k, j))
            return ans + cuts[j] - cuts[i]
        return dfs(0, len(cuts) - 1)




        # # 递归公式 切割 i 到 j 的最小成本 是内部切割的最小成本加上当前的成本

        # dp[i][j] = min(dp[i][k] + dp[k][j]) + (j - i) 
    
c= Solution()
n = 30
cuts = [13,25,16,20,26,5,27,8,23,14,6,15,21,24,29,1,19,9,3]
print(c.minCost(n, cuts))