from repository.studentrepository import Repository
from service.studentservice import Service
from ui.console import Interface

repository=Repository('C:\Apps\Pycharm\Practice\students')
service=Service(repository)
interface=Interface(service)
interface.menu()
