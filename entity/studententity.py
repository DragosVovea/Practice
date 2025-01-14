class Student:

    def __init__(self, id, name, group, grade):
        self._id = id
        self._name = name
        self._group = group
        self._grade = grade

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    def __str__(self):
        return f"{self._id},{self._name},{self._group},{self._grade}"
