class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0
        max_ones = 0

        print(len(nums))
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_ones = max(max_ones, count)
                count = 0 

        return max(max_ones, count)


