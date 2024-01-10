# 暴力法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index2 <= index1:
                    continue
                temp_sum = value1 + value2
                if temp_sum == target:
                    return [index1, index2]
        return []


# hash 法, 44 ms, 18.15 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        for index, value in enumerate(nums):
            if target - value in temp_dict:
                return [index, temp_dict.get(target - value)]
            temp_dict[value] = index
        return []