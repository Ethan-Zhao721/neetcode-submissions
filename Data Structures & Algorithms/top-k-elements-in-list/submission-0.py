class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)        
        
        sorted_d = dict(sorted(map.items(), key=lambda x: x[1], reverse=True))
        arr = []
        for i, (key,value) in enumerate(sorted_d.items()):
            if i < k: 
                arr.append(key)

        return arr
