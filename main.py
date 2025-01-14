from repository.studentrepository import Repository
from service.studentservice import Service
from ui.console import Interface

def main():
    repository=Repository('C:\Apps\Pycharm\Practice\students')
    service=Service(repository)
    interface=Interface(service)
    interface.menu()

if __name__ == '__main__':
    main()
