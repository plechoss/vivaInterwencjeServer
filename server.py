import flask
import requests
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

allegro_data = None
allegro_timestamp = datetime.now()


@app.route('/allegro', methods=['GET'])
def home():
    timestamp = datetime.now()
    if((allegro_data is None) or (timestamp - allegro_timestamp).seconds / 60):
        allegro_data = requests.get('https://w3schools.com/python/demopage.htm')
        print(allegro_data)
    return allegro_data, 200


app.run()
