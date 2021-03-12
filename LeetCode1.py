# using hashtable
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for index, num in enumerate(nums):
            if hashmap.get(target-num) is not None:
                return [index, hashmap.get(target-num)]
            hashmap[num] = index
