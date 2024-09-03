from flask import Flask, jsonify, send_file, Response
import requests
from flask_cors import CORS
from io import BytesIO
import sqlite3
import json
import gzip
from utils import getAllCaseNames, getCases
app = Flask(__name__)
CORS(app)

@app.route('/api/main-sections', methods=['GET'])
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
    return jsonify(response.json())

@app.route('/<id>/<image>', methods=['GET'])
def get_case_image(id, image):
    url = 'https://cdn.front.skin.club/{}/{}'.format(id, image)
    response = requests.get(url)
    return send_file(BytesIO(response.content), mimetype='image/jpeg')
@app.route("/api/cases/<caseName>", methods=['GET'])
def getCase(caseName):
    conn = sqlite3.connect('./skin.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM "{caseName}Weapons"')
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

    return jsonify(data)

@app.route("/api/main", methods=['GET'])
def createMainJson():
    cases = getAllCaseNames()
    arr = []
    for case in cases:
        case_data = getCases(case)
        arr.append({case: case_data})
        
    json_data = json.dumps(arr)
    compressed_data = gzip.compress(json_data.encode('utf-8'))
    
    response = Response(compressed_data, content_type='application/json')
    response.headers['Content-Encoding'] = 'gzip'
    response.headers['Content-Length'] = len(compressed_data)
    
    return response
if __name__ == '__main__':
    app.run(debug=True)