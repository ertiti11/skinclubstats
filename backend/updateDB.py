import sqlite3
import requests
def getCase(caseName):
    URL = "https://gate.skin.club/apiv2/cases/"+caseName
    data = requests.get(URL)
    return data.json()

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






def createDB():
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute("CREATE TABLE caseNAmes (name TEXT)")
    for case in caseNames:
        c.execute("INSERT INTO caseNAmes (name) VALUES (?)", (case,))
    conn.commit()
    conn.close()

allcases = get_main_sections()
caseNames = []

for type in allcases:
    for case in type["cases"]:
        caseNames.append(case["name"])
    
createDB()



def caseData2DB(caseName):
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute("CREATE TABLE cases (name TEXT,, price REAL, id INTEGER)")