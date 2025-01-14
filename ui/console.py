class Interface:
    def __init__(self, service):
        self._students_service = service

    @staticmethod
    def options():
        print("1. Afisare studenti\n2. Filtrare grupa\n3. Group count\n\tx. Exit")

    def menu(self):
        while True:
            self.options()
            command = input("Command:")
            if command == '1':
                self.afisare_studenti()
            elif command == '2':
                self.filtrare_grupa()
            elif command == '3':
                self.group_count()
            elif command == 'x':
                print("Bye!")
                break
            else:
                print("Comanda inexistenta")

    def afisare_studenti(self):
        students = self._students_service.get_students()
        print("ID,NAME,GROUP,GRADE")
        for student in students:
            print(str(student))

    def filtrare_grupa(self):
        group = input("Grupa:")
        students = self._students_service.filtrare_grupa(group)
        print("ID,NAME,GROUP,GRADE")
        for student in students:
            print(str(student))

    def group_count(self):
        groups=self._students_service.group_count()
        print("GRUPA,NUMAR STUDENTI")
        for group in groups:
            print(group[0],group[1])
