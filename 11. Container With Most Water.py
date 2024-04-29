class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        for i in range(len(height)):
            w = 1
            for j in range(i + 1, len(height)):
                if(height[i] <= height[j]): 
                    # print(7, height[i] * w)
                    if(maxArea < height[i] * w):
                        maxArea = height[i] * w
                elif(height[i] > height[j]):
                    # print(11, height[j] * w)
                    if(maxArea < height[j] * w): 
                        maxArea = height[j] * w
                w+=1
                # print(f"{height[i]}, {height[j]}")


        return maxArea
        



# 未完成test case 53/62