#coding: latin1

from flask import *

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
]

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/countries/<int:id>")
def get_country(id):
    for country in countries:
        if country['id'] == id:
            return country, 200

    return {"error": "Country not found"}, 404

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201

    return {"error": "Request must be JSON"}, 415

@app.route('/')
def index():
    return 'Hola a todos! :)'

@app.put("/countries/<int:id>")
def modify_country(id):
    if request.is_json:
        newCountry = request.get_json()

        for country in countries:
            if country[id] == id:
                for element in newCountry:
                    country[element] = newCountry[element]
                    return country, 200
                
    return {"error": "Request must be JSON"}, 415



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5050)
