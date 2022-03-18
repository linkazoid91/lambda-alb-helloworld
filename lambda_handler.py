### Imports
import os
import sys
import json
sys.path.insert(0, './package') # Load modules from local folder

from apig_wsgi import make_lambda_handler
import bottle
from bottle import route, run, template

# Setup for ALB usage
app = bottle.default_app()
lambda_handler = make_lambda_handler(app)

@route('/')
def hello_world():
    return {
        "message": "Eat Shit Patrick"
    }
