class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        number_of_students = len(students)
        student_sandwich_preference = Counter(students)
        print(student_sandwich_preference)
        
        for sandwich in sandwiches:
            if student_sandwich_preference[sandwich] > 0: 
                student_sandwich_preference[sandwich] -= 1
                number_of_students -= 1
            else:
                return number_of_students
            
        return number_of_students