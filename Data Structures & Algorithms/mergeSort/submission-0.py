# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs, s, e):

        if e - s + 1 <= 1:
            return pairs

        # the middle index of the array
        m = (s + e) // 2

        # sort the left half
        self.mergeSortHelper(pairs, s, m)

        # sort the right half
        self.mergeSortHelper(pairs, m+1, e)

        # merge the sorted halfs
        self.merge(pairs, s, m, e)    

        return pairs

    def merge(self, pairs: List[Pair], s, m, e) -> List[Pair]:
        
        # copy the sorted left and right halfs to temp arrays
        L = pairs[s:m+1]
        R = pairs[m+1: e+1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        # add the remaining elements if one list has elements remaining
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1