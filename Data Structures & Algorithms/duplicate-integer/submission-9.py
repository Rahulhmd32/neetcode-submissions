class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for i in range(len(nums)):
            if nums[i] in hashset:
                return hashset[nums[i]]
            else:
                hashset[nums[i]] = True
        return False        