class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 1. Remove duplicates and sort them
        # 2. Overwrite the original nums array in place
        nums[:] = sorted(list(set(nums)))
        
        # 3. Return the new length
        return len(nums)
