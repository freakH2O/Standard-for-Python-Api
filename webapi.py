#!/usr/bin/env python3


from flask import Flask,jsonify
from random import randint
from flask_cors import CORS, cross_origin
import io
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route("/")
@cross_origin()
def read():
    msgs = {'msg1':'This is the first message','msg2':'This is the Second message'}
    return jsonify(msgs)



if __name__ == '__main__':
    app.run(debug=True)
