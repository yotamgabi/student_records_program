import unittest

from classes.Course import Course
from classes.Student import Student
from classes.StudentCourseRegistry import StudentCourseRegistry


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.summer_2022 = StudentCourseRegistry("Summer", 2022)
        self.course1 = Course("Calculus")
        self.course2 = Course("algo")
        self.student1 = Student(123456, "Yotam", 30)
        self.student2 = Student(654321, "Gabi", 29)
        self.summer_2022 = StudentCourseRegistry("Summer", 2022)
        self.summer_2022.register_student_to_course(self.student1, self.course1)
        self.summer_2022.register_student_to_course(self.student1, self.course2)
        self.summer_2022.set_grade(self.student1, self.course1, 99.522)
        self.summer_2022.set_grade(self.student2, self.course1, 91.225)
        self.summer_2022.set_grade(self.student1, self.course2, 85.2)
        self.summer_2022.set_grade(self.student2, self.course2, 90)

    def tearDown(self):
        pass

    def test_constructor(self):
        # wanted values
        self.assertIsInstance(self.summer_2022, StudentCourseRegistry)
        self.assertDictEqual(self.summer_2022.open_semesters, {("Summer", 2022): self.summer_2022})
        # unwanted values, should raise ValueError if not in config.py
        self.assertRaises(ValueError, StudentCourseRegistry, "not a semester", 2022)
        self.assertRaises(ValueError, StudentCourseRegistry, "Summer", 1992)
        self.assertRaises(ValueError, StudentCourseRegistry, "not a semester", 1992)

    def test_register_and_courses_getter(self):
        self.assertEqual(self.summer_2022.courses_of(self.student1), [self.course1, self.course2])

    def test_grades_of(self):
        # Tests for calling the function by a student:]
        grades_student1 = {self.course1: 99.522, self.course2: 85.2}
        self.assertDictEqual(self.summer_2022.grades_of(self.student1), grades_student1)
        # Tests for calling the function by a course:
        grades_course1 = {self.student1: 99.522, self.student2: 91.225}
        self.assertDictEqual(self.summer_2022.grades_of(self.course1), grades_course1)

    def test_set_grade(self):
        # updating field:
        self.summer_2022.set_grade(self.student1, self.course1, 60)
        # Tests for calling the function by a student:]
        grades_student1 = {self.course1: 60, self.course2: 85.2}
        self.assertDictEqual(self.summer_2022.grades_of(self.student1), grades_student1)
        grades_course1 = {self.student1: 60, self.student2: 91.225}
        self.assertDictEqual(self.summer_2022.grades_of(self.course1), grades_course1)


if __name__ == '__main__':
    unittest.main()
