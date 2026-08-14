# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        s = 0
        e = len(pairs)-1

        self.quicksort_helper(pairs, s, e)

        return pairs


    def quicksort_helper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        
        # check if list is empty or a single element
        if (e-s+1 <= 1):
            return pairs

        pivot = pairs[e]
        left = s

        # swap elements if they are < pivot value
        for i in range(s,e,1):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        # swap pivot value
        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quicksort_helper(pairs, s, left-1) # left portion
        self.quicksort_helper(pairs, left+1, e) # right portion