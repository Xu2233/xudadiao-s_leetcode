class Solution(object):
    def countKConstraintSubstrings(self, s, k, queries):
        """
        :type s: str
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def sperateSub(s,queries):
            res = []
            for arrray in queries:
                res.append(s[arrray[0]:arrray[1]+1])
            return res
        
        # return sperateSub(s,queries)
        def isok(strings, k):
            left = 0
            right = 1
            dict_temp = {'0':0,'1':0}
            dict_temp[strings[left]] += 1
            count = 0
            if len(strings) < k:
                return 1
            else:
                while left != right and right < len(strings):
                #少数了，right到最右边的时候，left
                    if dict_temp['0'] >k or dict_temp['1'] >k:
                        left +=1
                        dict_temp[strings[left]] -= 1
                    else:
                        if right == len(strings)-1:
                            left+=1
                            dict_temp[strings[left]] -= 1
                            count += 1
                        else:
                            dict_temp[strings[right]]+=1
                            right += 1
                            count += 1


            return count  


        arr = sperateSub(s,queries)
        count = []
        for array in arr:
            count.append(isok(array,k))
        return count


c = Solution()
s = "0001111"
k =2
queries = [[0,6]]
print(c.countKConstraintSubstrings(s,k,queries))
