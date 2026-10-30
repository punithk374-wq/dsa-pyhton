class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0,len(numbers)-1
        s=0
        while r>l:
            s=numbers[l]+numbers[r]
            if s > target:
                r-=1
            elif s < target :
                l+=1
            else:
                return [l+1,r+1]
        