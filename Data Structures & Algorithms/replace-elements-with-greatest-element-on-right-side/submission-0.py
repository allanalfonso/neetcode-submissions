class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        list_length = len(arr)

        for i in range(list_length):
            max_so_far = -1
            
            for j in range(list_length-1,i,-1):
                max_so_far = max(max_so_far, arr[j])
            
            arr[i] = max_so_far

        arr[i] = -1

        return arr
        