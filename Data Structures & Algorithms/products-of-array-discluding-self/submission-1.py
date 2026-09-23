class Solution:
    def prefixProd(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)+1)

        for i in range (1, (len(nums)+1)):
            res[i] = res[i-1] * nums[i-1]
        
        return res
    

    def suffixProd(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)+1)

        for i in reversed(range(0, (len(nums)-1))):
            res[i] = res[i+1] * nums[i+1]
            
        return res


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        pre = self.prefixProd(nums)
        su = self.suffixProd(nums)

        for i in range(len(nums)):
            res[i] = pre[i] * su[i]
        
        return res