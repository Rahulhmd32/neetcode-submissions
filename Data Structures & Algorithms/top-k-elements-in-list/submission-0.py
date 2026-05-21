class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0) + 1
        bucket = [[] for b in range(len(nums)+1)]

        for num, count in freq.items():
            bucket[count].append(num)

        result = []

        for j in range(len(bucket) - 1,0,-1):
            for r in bucket[j]:
                result.append(r)
                if len(result)==k:
                    return result            