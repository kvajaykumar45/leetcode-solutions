class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        i = 0
        rotation = 0
        while students and rotation < len(students):
            if students[0] == sandwiches[i]:
                students.popleft()
                i += 1
                rotation = 0  
            else:
                students.append(students.popleft())
                rotation += 1  

        return len(students)
        
