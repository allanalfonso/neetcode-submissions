class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        list_length = len(nums)

        for i in range(list_length):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k