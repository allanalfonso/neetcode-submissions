class Solution:
    def binarySearch(self, arr, target) -> bool:
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2

            if target > arr[mid]:
                L = mid + 1
            elif target < arr[mid]:
                R = mid - 1
            else:
                return True
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        L = 0 
        R = len(matrix)-1
        row_length = len(matrix[0])-1

        while  L <= R:
            mid = (L + R) //2

            if matrix[mid][0] > target: 
                R = mid - 1
            elif matrix[mid][row_length] < target:
                L = mid + 1
            else:
                return self.binarySearch(matrix[mid], target)
        
        return False