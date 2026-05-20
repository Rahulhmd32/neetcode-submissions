class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = 0
        out = {}
        for i,n in enumerate(nums):
            res = target - n
            if res in out:
                return [out[res], i]
                break
            out[n] = i    
                    
              

                