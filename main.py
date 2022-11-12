from flask import *
import json,time

app = Flask(__name__)


#get request endpoint that returns some mock data
@app.route('/', methods=["GET"])
def home_page():
    data = {'page': 'home', 'time': time.time()}
    json_dump = json.dumps(data)
    return json_dump

if __name__=='__main__': app.run(port=7777)