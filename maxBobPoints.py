class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        
        """
        arrows_touse = 1
        arrows_now = numArrows
        while arrow_now > 0:
            for i in range(len(aliceArrows)):
                # 检查 Alice 是否在该区域射箭
                if aliceArrows[i] < arrows_touse:
                    # 在该区域射箭
                    aliceArrows[i] += arrows_touse
                    arrow_now -= arrows_touse
                    break
            else:
                # 如果所有区域都已经射过箭，增加 arrows_touse 的值
                arrows_touse += 1
                if arrows_touse > len(aliceArrows):
                    # 如果 arrows_touse 大于区域数，结束循环
                    break


        #包不是最大的

        print(bobArrows)

        return bobArrows
        

c = Solution()
c.maximumBobPoints(9,[1,1,0,1,0,0,2,1,0,1,2,0]
)