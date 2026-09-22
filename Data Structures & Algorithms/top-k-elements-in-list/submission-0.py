class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapping = {}

        buckets = [[] for _ in range(len(nums)+1)]
        for i in nums:
            mapping[i] = mapping.get(i,0)+1
        for number, freq in mapping.items():
            buckets[freq].append(number)

        result = []

        for i in range(len(nums), 0, -1):
            for s in buckets[i]:
                result.append(s)
            
            if len(result) == k:
                return result



        