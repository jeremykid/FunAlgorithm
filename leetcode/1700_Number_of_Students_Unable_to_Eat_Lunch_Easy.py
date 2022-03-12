class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # method 1
        count = 0
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            elif count > len(students): # one loop
                break
            else:
                x = students.pop(0) #student go to the end of line
                students.append(x)
                count += 1 # count one sandwiches don't like