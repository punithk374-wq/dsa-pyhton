class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        window = SortedList()
        
        for j in range(l, n + 1):
            window.add(prefix[j - l])
            if j - r - 1 >= 0:
                window.remove(prefix[j - r - 1])
                
            idx = window.bisect_left(prefix[j])
            if idx > 0:
                min_sum = min(min_sum, prefix[j] - window[idx - 1])
                
        return min_sum if min_sum != float('inf') else -1
        
        