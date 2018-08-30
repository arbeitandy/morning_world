from flask import Flask
from flask import request
from flask import json
import os
import logging
from flask.logging import default_handler


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(DEBUG=True)
    logging.basicConfig(filename='error.log', level=logging.DEBUG)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def morning_world():
        """
            1. request header without Accept
               output: hello world
            2. header with "Accept: application/json"
               output: json message
            3. corner case: has "Accept" but not accept json
        """

        PLAIN_MSG = '<p>Morning World<p>'
        JSON_MSG = {'message': 'Good morning'}

        if request.headers['Accept'] != 'application/json':
            return PLAIN_MSG
        else:
            response = Response(
                                json.dumps(JSON_MSG),
                                status=200,
                                mimetype='application/json'
                                )
            return response


        return app
