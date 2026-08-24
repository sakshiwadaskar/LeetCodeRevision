class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} # num -> freq 
        
        for n in nums:
            freqMap[n] = 1 +  freqMap.get(n,0)

        arr = [[] for _ in range(0, len(nums) + 1)]

        for n, freq in freqMap.items():
            arr[freq].append(n)
        res = []
        for i in range(len(arr)-1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
        