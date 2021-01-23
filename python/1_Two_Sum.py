class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for index1 in range(length):
            for index2 in range(length):
                if (index1 == index2):
                    pass
                elif ((nums[index1] + nums[index2]) == target):
                    return [index1, index2]
                
        return []
