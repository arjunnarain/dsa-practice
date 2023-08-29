# 1700. Number of Students Unable to Eat Lunch
#link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
from ast import List

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
    
# solution using queue 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        
    def dequeue(self):
        if not self.front:
            return None
        removed = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return removed.value
    
    def is_empty(self):
        return self.size == 0
    
class Solution:
    def countStudents(self, students: [int], sandwiches: [int]) -> int:
        queue_0 = Queue()
        queue_1 = Queue()
        
        # Distribute students into queues based on their preference
        for student in students:
            if student == 0:
                queue_0.enqueue(student)
            else:
                queue_1.enqueue(student)
        
        # Process sandwiches
        for sandwich in sandwiches:
            if sandwich == 0:
                if queue_0.is_empty():
                    break
                queue_0.dequeue()
            else:
                if queue_1.is_empty():
                    break
                queue_1.dequeue()
        
        # Return the total number of students still in the queues
        return queue_0.size + queue_1.size
