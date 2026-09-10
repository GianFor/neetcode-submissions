class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        res = [-1, -1]

        for (i,n) in enumerate(nums):
            indices[n] = i
        
        for (i,n) in enumerate(nums):
            diff = target-n
            if diff in indices and indices[diff] != i:
                res[0] = i
                res[1] = indices[diff]
                return res
        
        return res