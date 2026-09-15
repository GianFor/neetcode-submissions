class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        res = []
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        
        for key,v in sorted(cnt.items(), key = lambda item : item[1], reverse=True):
            if k>0:
                res.append(key)
                k -= 1
            else:
                break
        return res
