class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        count = 0

        for n in nums:
            hashMap[n] = 1

        for n in hashMap.keys():
            if n-1 in hashMap.keys(): continue
            curr = 1
            while n+1 in hashMap.keys():
                n += 1
                curr += 1
            count = max(curr, count)

        return count
