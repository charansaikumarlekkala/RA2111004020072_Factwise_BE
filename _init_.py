from concrete.user_impl import UserImpl
from concrete.team_impl import TeamImpl
from concrete.board_impl import BoardImpl
from concrete.task_impl import TaskImpl

def get_all_users():
          return UserImpl.get_all()
def get_all_teams():
          return TeamImpl.get_all()
def get_all_boards():
          return BoardImpl.get_all()
def get_all_tasks():
          return TaskImpl.get_all()
                                        
