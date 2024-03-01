import json
from flask import request, Flask, jsonify
import requests
app = Flask(__name__)


@app.route('/', methods=['GET'])
def test_app():
    return jsonify({"test": "app"})


@app.route('/weather_data', methods=['GET'])
def get_weather_data():
    params = {
        'access_key': '5d9eaebb3b830bdd7daf5260abb458c3',
        'query': request.args['query']
    }
    r = requests.get('http://api.weatherstack.com/current', params)

    response = jsonify(r.json())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run()
