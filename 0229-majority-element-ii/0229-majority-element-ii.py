class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        threshold = len(nums) // 3
        c1_actual = nums.count(cand1) if count1 > 0 else 0
        c2_actual = nums.count(cand2) if count2 > 0 and cand2 != cand1 else 0
        
        if c1_actual > threshold:
            result.append(cand1)
        if c2_actual > threshold:
            result.append(cand2)
            
        return result
