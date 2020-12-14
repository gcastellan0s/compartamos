from flask import Flask, request, jsonify, Response
from bson.json_util import dumps
from flask_cors import CORS

from pymongo import MongoClient
from twilio.rest import Client

app = Flask(__name__)

CORS(app)
#CORS(app, resources={r"/api/*": {"origins": "0.0.0.0:8080"}})

app.config["DEBUG"] = True
client = MongoClient('mongodb://debug:debug@mongo:27017')
twilio = Client('ACa28eb624104391fcf176479f3eacc57a', '6e018782abf1c8aa5dc181422a1e046b')

@app.route('/api/v1/getNip', methods=['GET'])
def getNip():
    params = {}
    for args in request.args:
        if not args == 'numero_movil':
            params[args] = {'$regex': request.args[args]}
    resp = list(client.clientes.cuentas.aggregate([
        {'$match': params},
    ]))[0]
    twilio.messages.create(
        to="+521" + request.args['numero_movil'],
        from_="+14242968994",
        body="Tu NIP es: " + resp['nip']
    )
    return Response(dumps(resp), status=200, mimetype='application/json')

##########################
app.run(host='0.0.0.0')
