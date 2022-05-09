from classes.Course import Course


class Student:
    def __init__(self, student_id: int, name: str, age: int):
        self._id = student_id
        self._name = name
        self._age = age

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


