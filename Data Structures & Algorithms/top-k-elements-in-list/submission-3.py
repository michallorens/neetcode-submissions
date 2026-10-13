class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n in counts.keys():
                counts[n] += 1
            else:
                counts[n] = 1

        return [k for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]]
        