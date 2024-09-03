import sqlite3

def getAllCaseNames():
    conn = sqlite3.connect("./skin.db")
    c = conn.cursor()
    c.execute    ("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE '%weapons%' AND name NOT LIKE '%casenames%'")
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]



def getCase(caseName):
    conn = sqlite3.connect("./skin.db")
    c = conn.cursor()
    c.execute(f'SELECT * FROM "{caseName}Weapons"')
    rows = c.fetchall()

    # Obtener los nombres de las columnas
    column_names = [description[0] for description in c.description]
    case_price = c.execute(f'SELECT price FROM "{caseName}"').fetchone()[0]
    conn.close()

    # Convertir las filas en una lista de diccionarios
    data = []
    data.append({"price": case_price})
    for row in rows:
        row_dict = dict(zip(column_names, row))
        # Convertir price a int si es posible
        if "price" in row_dict and row_dict["price"].is_integer():
            row_dict["price"] = int(row_dict["price"])
        data.append(row_dict)

    return data


def profit_chance(data):
    profit_chance = 0
    for weapon in data:
        if weapon["price"] > data[0]["price"]:
            profit_chance += weapon["chance"]
    return profit_chance


def profit_chanceX1dot5(data):
    profit_chance = 0
    for weapon in data:
        if weapon["price"] > data[0]["price"] * 1.5:
            profit_chance += weapon["chance"]
    return profit_chance


def profit_chanceX2(data):
    profit_chance = 0
    for weapon in data:
        if weapon["price"] > data[0]["price"] * 2:
            profit_chance += weapon["chance"]
    return profit_chance


def profit_chanceX3(data):
    profit_chance = 0
    for weapon in data:
        if weapon["price"] > data[0]["price"] * 3:
            profit_chance += weapon["chance"]
    return profit_chance


def profit_chanceX10(data):
    profit_chance = 0
    for weapon in data:
        if weapon["price"] > data[0]["price"] * 10:
            profit_chance += weapon["chance"]
    return profit_chance


# detectar la skin mas barata
def min_price(data):
    caseprice = data[0]["price"]
    minprice = caseprice
    for weapon in data:
        if weapon["price"] < minprice:
            minprice = weapon["price"]
    return (caseprice - minprice) / 100


def calculate_EV(data):
    EV = 0
    for weapon in data:
        try:
            EV += weapon["price"] * weapon["chance"]
        except:
            pass
    return EV / 10000


def calculate_IRB(data):
    # (EV * (profitChance + 0.5 * oneFiveChance + 0.75 * doubleChance + tripeChance)) / casePriceNum
    EV = calculate_EV(data)
    profitChance = profit_chance(data)
    oneFiveChance = profit_chanceX1dot5(data)
    doubleChance = profit_chanceX2(data)
    tripleChance = profit_chanceX3(data)
    casePriceNum = data[0]["price"]
    return (
        (EV * (profitChance + 0.5 * oneFiveChance + 0.75 * doubleChance + tripleChance))
        / casePriceNum
    ) * 100





def getAllStatFromCase(caseName):
    case = getCase(caseName)
    image = case[1]["image"]
    profit = profit_chance(case)
    profit1dot5 = profit_chanceX1dot5(case)
    profit2 = profit_chanceX2(case)
    profit3 = profit_chanceX3(case)
    profit10 = profit_chanceX10(case)
    minprice = min_price(case)
    ev = calculate_EV(case)
    irb = calculate_IRB(case)
    
    conn = sqlite3.connect("./skin.db")
    c = conn.cursor()
    c.execute(f'UPDATE "{caseName}" SET profit_chance = ?, profit_chanceX1dot5 = ?, profit_chanceX2 = ?, profit_chanceX3 = ?, profit_chanceX10 = ?, real_price = ?, ev = ?, irb = ?, image = ?', (profit, profit1dot5, profit2, profit3, profit10, minprice, ev, irb, image))
    conn.commit()
    conn.close()




def main():
    cases = getAllCaseNames()
    for case in cases:    
        getAllStatFromCase(case)
    print("Proceso terminado")



main()
