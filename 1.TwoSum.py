class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnList: List[int] = []
        if (len(nums) < 2 or len(nums) > (10**4) or target < (-10 ** 9) or target > (10 ** 9)):
            return returnList
        for i in range(len(nums)):
           if( nums[i] < (-10 ** 9) or nums[i] > (10 ** 9)):
                continue   
           for j in range(i+1 ,len(nums)):
                if((nums[i]+nums[j]) == target):
                    returnList.append(i)
                    returnList.append(j)
                    return returnList