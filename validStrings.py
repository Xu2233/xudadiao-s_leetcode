class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        有效字符串即不含相邻的 0
        初始化一个空字符串作为当前解。
        递归地添加字符到当前解中，每次添加后检查是否满足条件。
        如果当前解的长度等于 n, 则将其添加到结果列表中。
        继续递归直到所有可能的字符串都被检查。
        """
        res =[]

        def backtrack(path):
            if len(path) == n:
                res.append(path)
                
    



        