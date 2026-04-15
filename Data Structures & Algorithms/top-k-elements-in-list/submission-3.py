class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for num in nums:
            f[num] = f.get(num, 0) + 1

        return sorted(f.keys(), key=lambda x: f[x], reverse=True)[:k]
            
