class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        circle_sandwiches = sandwiches.count(0)
        square_sandwiches = sandwiches.count(1)
        students_who_like_circle_sandwiches = students.count(0)
        students_who_like_square_sandwiches = students.count(1)
        
        for sandwich in sandwiches:
            if sandwich == 0 and students_who_like_circle_sandwiches > 0:
                students_who_like_circle_sandwiches -= 1
            elif sandwich == 1 and students_who_like_square_sandwiches > 0:
                students_who_like_square_sandwiches -= 1
            else:
                break

        return students_who_like_circle_sandwiches + students_who_like_square_sandwiches

        

        # result = [i for i in arr if i % 2 == 0]
        # result = [i + j for i, j in zip(arr1, arr2)]
        # all(a == -b for a, b in zip(list1, list2)):