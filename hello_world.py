from flask import Flask
from flask import request
from flask import json
from flask import Response

import logging
from flask.logging import default_handler

app = Flask(__name__)
app.config.from_pyfile('config.py')
logging.basicConfig(filename='error.log', level=logging.DEBUG)
# LOGGER = logging.getLogger(__name__)



@app.route('/')
def hello_world():
    """
        1. request header without Accept
           output: hello world
        2. header with "Accept: application/json"
           output: json message
        3. corner case: has "Accept" but not accept json
    """

    PLAIN_MSG = '<p>Hello World<p>'
    JSON_MSG = {'message': 'Good morning'}

    if request.headers['Accept'] != 'application/json':
        return PLAIN_MSG
    else:
        # request.headers['Accept'] == 'application/json':           
        response = Response(
                            json.dumps(JSON_MSG),
                            status=200,
                            mimetype='application/json'
                            )
        return response


if __name__ == '__main__':
    app.run()
