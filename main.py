# my_student = {
#     "name": "Rolf Smith",
#     "grades": [70, 88, 90, 99]
# }

# def avarage_grade(student):
#     return sum(student["grades"]) / len(student["grades"])

# print(avarage_grade(my_student))







# my_student = {
#     "name": "Rolf Smith",
#     "grades": [70, 88, 90, 99]
# }

# def avarage_grade(student):
#     return sum(student["grades"]) / len(student["grades"])

# print(avarage_grade(my_student))

class Sudent:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avarage(student):
        return sum(student.grades) / len(student.grades)

student_one = Sudent("Ali Mirzaev", [91, 90, 95, 98, 100])

print(student_one.avarage())


















