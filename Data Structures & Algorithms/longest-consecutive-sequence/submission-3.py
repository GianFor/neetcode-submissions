class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = sorted(list(set(nums)))
        absoluteSeq = 1 if nums else 0
        localSeq = 1

        for i in range(1, len(numbers)):
            if(numbers[i]==(numbers[i-1]+1)):
                localSeq += 1
            else:
                localSeq = 1
            
            absoluteSeq = max(absoluteSeq, localSeq)
                
        return absoluteSeq