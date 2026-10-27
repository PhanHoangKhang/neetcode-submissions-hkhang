class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_count = 0

        arr = set(nums)

        for num in arr:
            count = 0
            if num - 1 not in arr:
                while num in arr:
                    num+=1
                    count+=1
            
            longest_count = max(longest_count, count)

        return longest_count

