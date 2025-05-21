#######################
BASE DE DATOS CHIVATO  

import sqlite3
import re

#bloque base de datos
def create_table(path=':memory:'):
  con = sqlite3.connection(path)
  cur = con.cursor()
  con.row_factory = sqlite3.row
  
  sql = """ CREATE TABLE game (
  id INT PRIMARY KEY,
  player_1 TEXT,
  player_2 TEXT,
  decision_1 TEXT,
  decision_2 TEXT,
  point_1 INT NOT NULL,
  point_2 INT NOT NULL
  )

  """
  cur.execute(sql)
  con.commit()
  con.close()

#FUNCIONES
def calculate_point (decision_1, decision_2):
  match (decision_1, decision_2):
    case (True, True):
      return (3, 3)
    case (True, False):
      return (0, 7)
    case (False, False):
      return (1, 1)
    case (False, True):
      return (7, 0)


















def save_decision(decision_1: str, decision_2: str) -> None:
  sql = 'INSERT INTO activity(player_1, player_2, decision_1, decision_2) VALUES(?, ?, ?, ?)'
  cur.execute(sql, (decision_1, decision_2))
  con.commit()

def calculate_points(decision_1, decision_2):
  player_1 = 'SELECT decision_1 '
  
             
def loquesea()
