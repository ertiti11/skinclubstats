import sqlite3


def getAllCaseNames():
    conn = sqlite3.connect("./skin.sqlite")
    c = conn.cursor()
    c.execute    ("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE '%weapons%' AND name NOT LIKE '%casenames%'")
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]