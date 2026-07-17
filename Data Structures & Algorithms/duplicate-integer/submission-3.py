class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        values = list(freq.values())
        print(values)

        for value in values:
            if value > 1:
                return True

        return False