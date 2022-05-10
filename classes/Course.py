class Course:

    def __init__(self, course_name: str) -> object:
        self._name = course_name
        # Scalable part of code

    @property
    def name(self):
        return self._name
