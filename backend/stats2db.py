import sqlite3


def getCase(caseName):
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM "{caseName}Weapons"')
    rows = c.fetchall()
    
    # Obtener los nombres de las columnas
    column_names = [description[0] for description in c.description]
    case_price = c.execute(f'SELECT price FROM "{caseName}"').fetchone()[0]
    conn.close()



    # Convertir las filas en una lista de diccionarios
    data = []
    data.append({'price': case_price})
    for row in rows:
        row_dict = dict(zip(column_names, row))
        # Convertir price a int si es posible
        if 'price' in row_dict and row_dict['price'].is_integer():
            row_dict['price'] = int(row_dict['price'])
        data.append(row_dict)

    return data



def profit_chance(caseName):
    data = getCase(caseName)
    profit_chance = 0
    for weapon in data:
        if weapon['price'] > data[0]['price']:
            profit_chance += weapon['chance']
    return profit_chance

def profit_chanceX1dot5(caseName):
    data = getCase(caseName)
    profit_chance = 0
    for weapon in data:
        if weapon['price'] > data[0]['price']*1.5:
            profit_chance += weapon['chance']
    return profit_chance

def profit_chanceX2(caseName):
    data = getCase(caseName)
    profit_chance = 0
    for weapon in data:
        if weapon['price'] > data[0]['price']*2:
            profit_chance += weapon['chance']
    return profit_chance

def profit_chanceX3(caseName):
    data = getCase(caseName)
    profit_chance = 0
    for weapon in data:
        if weapon['price'] > data[0]['price']*3:
            profit_chance += weapon['chance']
    return profit_chance

def profit_chanceX10(caseName):
    data = getCase(caseName)
    profit_chance = 0
    for weapon in data:
        if weapon['price'] > data[0]['price']*10:
            profit_chance += weapon['chance']
    return profit_chance


#detectar la skin mas barata
def min_price(caseName):
    data = getCase(caseName)
    caseprice = data[0]['price']
    minprice = caseprice
    for weapon in data:
        if weapon['price'] < minprice:
            minprice = weapon['price']
    return (caseprice - minprice) / 100

def calculate_EV(caseName):
    data = getCase(caseName)
    EV = 0
    for weapon in data:
        try:
            EV += weapon['price'] * weapon['chance']
        except:
            pass
    return EV/10000
  




print(calculate_EV('covert')) # 0.0