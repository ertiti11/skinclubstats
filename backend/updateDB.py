import sqlite3
import requests
import time


def deleteAllTables():
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    for table in tables:
        c.execute(f'DROP TABLE "{table[0]}"')
    conn.commit()
    conn.close()

deleteAllTables()

def getCase(caseName):
    URL = "https://gate.skin.club/apiv2/cases/"+caseName
    data = requests.get(URL)
    return data.json()["data"]

def get_main_sections():
    url = 'https://gate.skin.club/api/main-sections?page=1&per-page=100'
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "es-,es;q=0.8",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjIyNjUzOTEsInYiOjIsImlhdCI6MTcyMzM5NjU5OS42MzcxNDgsImV4cCI6MTcyMzM5ODM5OS42MzcxNDl9.OGwzierKC7kC3GwxjTQUev0eeTLtMdrDycvMVF_q_EY",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "x-amplitude-device-id": "dj4SwAwI0ne9tIPNkjgxhS",
        "x-amplitude-session-id": "1723396605945",
        "x-requested-with": "XMLHttpRequest",
        "x-site-mode": "original"
    }
    response = requests.get(url, headers=headers)
    return (response.json()["data"])

def deleteCaseNameTable():
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS caseNames")
    conn.commit()
    conn.close()

def createDB():
    deleteCaseNameTable()
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS caseNames (name TEXT)")
    for case in caseNames:
        c.execute("INSERT INTO caseNames (name) VALUES (?)", (case,))
    conn.commit()
    conn.close()

allcases = get_main_sections()
caseNames = []

for type in allcases:
    for case in type["cases"]:
        caseNames.append(case["name"])
    




def caseData2DB(caseName):
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute(f'CREATE TABLE IF NOT EXISTS "{caseName}" (price REAL, profit_chance REAL, profit_chanceX1dot5 REAL, profit_chanceX2 REAL, profit_chanceX3 REAL, profit_chanceX10 REAL, real_price REAL, ev REAL, irb REAL)')
    c.execute(f'CREATE TABLE IF NOT EXISTS "{caseName}Weapons" (id INTEGER PRIMARY KEY, name TEXT, price REAL, rarity TEXT, image TEXT, finish TEXT, chance REAL)')
    data = getCase(caseName)

    c.execute(f'INSERT INTO "{caseName}" (price) VALUES (?)', (data["price"],))
    
    for weapon in data["last_successful_generation"]["contents"]:
        image = weapon["item"]["file"]["path"]
        if image is not None:
            c.execute(f'INSERT INTO "{caseName}Weapons" (name, price, rarity, image, finish, chance) VALUES (?,?,?,?,?,?)', 
                      (weapon["item"]["market_hash_name"], weapon["fixed_price"], weapon["item"]["rarity_site"], image, weapon["item"]["finish"], weapon["chance_percent"]))
            conn.commit()
        else:
            print(f"Advertencia: La clave 'image' no se encontró en el arma {weapon['item']['market_hash_name']}")
    
    conn.close()

createDB()
print(len(caseNames))
print("insertando armas en la base de datos...")
started = time.time()
for case in caseNames:
    caseData2DB(case)

print(f"Proceso terminado en {time.time()-started} segundos")







