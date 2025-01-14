from util.utility_functions import transform_dict_in_list_of_tuples
class Service:
    def __init__(self, repository):
        self._students_repository = repository

    def get_students(self):
        return self._students_repository.get_students()

    def filtrare_grupa(self, group):
        students = self._students_repository.get_students()
        filtered_students = []
        for student in students:
            if student.group == group:
                filtered_students.append(student)
        return filtered_students

    def group_count(self):
        groups = {}
        students = self._students_repository.get_students()
        for student in students:
            if student.group not in groups.keys():
                groups[student.group] = 1
            else:
                groups[student.group] += 1
        groups=transform_dict_in_list_of_tuples(groups)
        return groups

