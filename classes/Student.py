from classes.Course import Course


def new_course(course_name: str):
    return Course(course_name)


class Student:
    _class = {}  # map student id to objects
    _trash = {}  # map student id to objects

    def __init__(self, student_id: int, name: str, age: int):
        self._id = student_id
        self._name = name
        self._age = age
        self._courses = {}
        self._class[student_id] = self

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def courses(self):
        return self._courses

    @property
    def grades(self):
        grades = {}
        for course_obj in self._courses.keys():
            if course_obj in


    def sign_to_course(self, course_obj: Course):
        self._courses[course_obj] = None  # course OBJECT -> @todo: decide what to map to

    def set_grade(self, course_obj: Course, grade: float):
        course_obj.set_grade(self, grade)

    def remove(self):
        del self._courses[self.id]
        self._trash[self.id] = self

        @todo
        # remove student grades from all courses
