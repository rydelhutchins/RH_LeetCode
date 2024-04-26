class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for index, element in enumerate(nums):
            num = target - element
            if element in hash_nums:
                hash_nums[element].append(index)
            else:
                hash_nums[element] = [index]
            if num in hash_nums:
                hash_index = hash_nums[num]
            else:
                continue
            if num in hash_nums and len(hash_index) > 1:
                return sorted([index, hash_index[0]])
            elif num in hash_nums and hash_index[-1] != index:
                return sorted([index, hash_index[-1]])