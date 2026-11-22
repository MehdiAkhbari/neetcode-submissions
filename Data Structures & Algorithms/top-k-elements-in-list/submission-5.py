class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        mydict = {}
        for i in range(len(nums)):
            mydict[nums[i]] = mydict.get(nums[i], 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        # print(freq)
        for key, val in mydict.items():
            freq[val].append(key)
            # print(val, key)
        for i in range(len(freq) - 1, -1, -1):
            for element in freq[i]:
                out.append(element)
                if len(out) == k:
                    return out
            
