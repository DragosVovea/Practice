from entity.studententity import Student
class Repository:

    def __init__(self, file_name):
        self._students_list = []
        self._file_name = file_name
        self.read_data()

    def read_data(self):
        with open(self._file_name, 'r') as file:
            for line in file:
                credentials = line.split(",")
                id = int(credentials[0])
                name = credentials[1]
                group = credentials[2]
                grade = float(credentials[3])
                student = Student(id, name, group, grade)
                self._students_list.append(student)

    def get_students(self):
        return self._students_list