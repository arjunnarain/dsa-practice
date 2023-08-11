# 1700. Number of Students Unable to Eat Lunch
#link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and students.count(sandwiches[0]) != 0:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students.pop(0))
        return len(students)
            

# alternative solution
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {0: 0, 1: 0}
        for student in students:
            count[student] += 1
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break
            count[sandwich] -= 1
        return sum(count.values())
