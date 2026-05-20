class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        res = 0 
        for i in num:
            if i-1 not in num:
                start = 0
                while i+start in num:
                    start += 1
                res = max(start, res)
        return res            