"""
    este script convierte la base de datos antigua a la nueva, cogiendo los datos
    de la antigua base de datos y transformando los datos a la nueva base de datos
"""

import sqlite3
from utils import getAllCaseNames



def casenames_to_new_db():
    casenames = getAllCaseNames()
    conn = sqlite3.connect("../skins_database.sqlite")
    c = conn.cursor()
    for case in casenames:
        c.execute("INSERT INTO cases (case_name) VALUES (?)", (case,))
        conn.commit()
    conn.close()







def old_to_new_db():

    casenames_to_new_db()
    
  









old_to_new_db()



    