#######################
import sqlite3
from __future__ import annotations
DB_PATH = ':memory:'

#bloque base de datos
class Db_Handler:
  def __init__(self, db_path: str =DB_PATH):
    self.con = sqlite3.connect(db_path)
    self.con.row_factory = sqlite3.Row
    self.cur = self.con.cursor()
    
  def create_table():
    sql = """ CREATE TABLE game (
    id INT PRIMARY KEY,
    point_1 INT NOT NULL,
    point_2 INT NOT NULL
    )
    """
    self.cur.execute(sql)
    self.con.commit()

#FUNCIONES
class SavedInfo(db_handler):
  def __init__(self):
    super().__init__()
    point_1, point_2 = point_round()
    
  def save_decision(self) -> None:
    sql = 'INSERT INTO game (point_1, point_2) VALUES (?,?)'
    self.cur.execute(sql,(point_1, point_2))
                     
  def count_point() -> int:
    total_point_1 = list(self.cur.execute('SELECT SUM(point_1) AS total_points_1')).fetchone()[0]
    total_point_2 = list(self.cur.execute('SELECT SUM(point_2) AS total_points_2')).fetchone()[0]
    return int(total_point_1), int(total_point_2)
    
def decision(other_decision: bool) -> bool:
  match other_decision:
    case False:
      return True
    case True:
      return True
    case _:
      return True

def point_round(decision_1=True, decision_2=other_decision):
  match (decision_1, decision_2):
    case (True, True):
      return (3, 3)
    case (True, False):
      return (7, 0)
    case (False, False):
      return (1, 1)
    case (False, True):
      return (0, 7)



def winner() -> str:
  player1, player2 = save.count_point()
  if player1 > player2:
    return 'Player1 wins'
  elif player2 > player1:
    return 'Player2 wins'
  else:
    return 'Empate'
    
