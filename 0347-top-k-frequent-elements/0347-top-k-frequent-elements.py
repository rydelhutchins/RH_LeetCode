from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)
        output = []
        for num in nums:
            frequency_map[num] += 1
        for i in range(k):
            key_of_max_value = max(frequency_map, key=frequency_map.get)
            output.append(key_of_max_value)
            del frequency_map[key_of_max_value]
        return output