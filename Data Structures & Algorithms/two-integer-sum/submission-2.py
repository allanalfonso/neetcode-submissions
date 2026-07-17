class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = []
        hashmap = {} # val, index

        for index, value in enumerate(nums):

            diff = target - value

            if diff in hashmap:
                return [hashmap[diff],index]
                #indices.append(hashmap[diff])
                #indices.append(index)
            else:
                hashmap[value] = index

        return indices
            