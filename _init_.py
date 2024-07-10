import json
import os
from datetime import datetime
from project_board_base import
ProjectBoardBase

DB_PATH='db/'

class 
ProjectBoard(ProjectBoardBase):
          def_init_(self):
            if not
       os.path.exists(DB_PATH):
             os.makedirs(DB_PATH)
          def_load_data(set,filename):
            filepath=os.path.join(DB_PATH)
              if os.path.exists(filepath):
                 with open(filepath,'r')as
       file:
                   return json.load(file)
             return{}

          def_save_data(self,filename,data):
            filepath=os.path.join(DB_PATH,filename)
                  with open(filepath,'w')as file:
                    json.dump(date,file,indent=4)
          def create_board(self,request:str)->str:
            data=json.loads(request)
            team_id=data['team_id']
            boards=self._load_data('board.json')
