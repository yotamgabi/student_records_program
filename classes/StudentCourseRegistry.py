from classes.Course import Course
from classes.Student import Student
import classes.config as cfg


class StudentCourseRegistry:
    _open_semesters = {}

    def __init__(self, semester: str, year: int):
        self._open_semesters[(semester, year)] = self
        self._grades_per_course = {}  # maps to a dict of: student -> grades
        self._student_to_courses = {}
        """
        maps each student to courses list. note that the list is vert much finite meaning:
        O(1) space and time complexity when we lookup course-to-student 
        """

        # allowed properties for constructor in classes \ config.py
        if semester in cfg.possible_semesters:
            self._semester = semester
        else:
            raise ValueError(f"Semester can be only: {cfg.possible_semesters}")
        if year in cfg.possible_years:
            self._year = year
        else:
            raise ValueError(f"Year can be only: {cfg.possible_years}")

    def register_student_to_course(self, student: Student, course: Course):
        if student in self._student_to_courses:
            self._student_to_courses[student].append(course)
        else:  # new student, first time to register
            self._student_to_courses[student] = [course]

    def courses_of(self, student: Student):
        return self._student_to_courses[student]

    def grades_of(self, course_or_student):  # can get course or student as input
        if type(course_or_student) == Student:
            student_grades = {}
            for course in self._grades_per_course.keys():
                course_grade = self._grades_per_course[course][course_or_student]
                if course_grade:
                    student_grades[course] = course_grade
            return student_grades
        else:
            return self._grades_per_course[course_or_student]

    def set_grade(self, student: Student, course: Course, grade: float):
        if course in self._grades_per_course:
            self._grades_per_course[course][student] = grade
        else:  # new course data
            self._grades_per_course[course] = {student: grade}
    @property
    def open_semesters(self):
        return self._open_semesters
