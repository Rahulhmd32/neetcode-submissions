class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prod = 1
        zer_cnt = 0
        for i in nums:
            if i == 0:
                zer_cnt += 1
            else:
                prod *= i
        if zer_cnt>1:
            res = [0]*len(nums)
            return res
        for i,n in enumerate(nums):
            if zer_cnt == 1:
                if n == 0:        
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod//n
        return res         

