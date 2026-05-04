class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)        
        sorted_d = sorted(map, key=map.get, reverse=True)
        return sorted_d[:k]
