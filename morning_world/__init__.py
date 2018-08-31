from flask import Flask
from flask import request
from flask import jsonify

import os
import logging
from logging import Formatter, FileHandler
from flask.logging import default_handler


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    logging.basicConfig(
                level=logging.DEBUG,
                filename='error.log',
                filemode='a'
                )

    fh = logging.FileHandler(filename='error.log')

    FORMAT = "[%(asctime)s] %(url)s"
    formatter = RequestFormatter(fmt=FORMAT)
    #formatter = logging.Formatter('%(asctime)s')
    fh.setFormatter(formatter)

    app.logger.removeHandler('werkzeug')
    app.logger.addHandler(fh)
    if not app.debug:
        app.logger.setLevel(logging.INFO)
    else:
        app.logger.setLevel(logging.DEBUG)

    # enable testing
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # routing - would move to individual file 
    @app.route('/')
    def root_path():
        """
            1. request header without Accept
               output: hello world
            2. header with "Accept: application/json"
               output: json message
            3. corner case: has "Accept" but not accept json
        """

        PLAIN_MSG = '<p>Morning World!</p>'
        JSON_MSG = {'message': 'Good morning'}

        if request.headers['Accept'] != 'application/json':
            return PLAIN_MSG
        else:
            return jsonify(JSON_MSG), 200


    return app

# inject request 
class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)
