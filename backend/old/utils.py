import sqlite3, json
def getAllCaseNames():
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute(f'SELECT name FROM "caseNames"')
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]


def getCases(caseName):
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute(f'SELECT price, profit_chance, profit_chanceX1dot5, profit_chanceX2, profit_chanceX3, profit_chanceX10, real_price, ev, irb, image FROM "{caseName}"')
    rows = c.fetchall()
    
    # Obtener los nombres de las columnas
    column_names = [description[0] for description in c.description]
    conn.close()

    # Convertir las filas en una lista de diccionarios
    data = []
    for row in rows:
        row_dict = dict(zip(column_names, row))
        # Convertir price a int si es posible
        if 'price' in row_dict and row_dict['price'].is_integer():
            row_dict['price'] = int(row_dict['price'])
        data.append(row_dict)
    
    return data




