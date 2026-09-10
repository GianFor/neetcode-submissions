class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_list = {}
        for i in nums:
            if(number_list.get(i) is None):
                number_list[i] = True
            else:
                return True
        return False