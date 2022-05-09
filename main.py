from classes.StudentCourseRegistry import StudentCourseRegistry
from classes.Course import Course
from classes.Student import Student
import classes.config as cfg

if __name__ == '__main__':
    math = Course("math")
    student_list = [Student(12346, "Yotam",30 ), Student(123123, "Hagai" ,25 )]
    summer_2022 = StudentCourseRegistry("Summer", 2022)

    print ()