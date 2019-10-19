# -*- coding: UTF-8 -*-
"""
Project Camptalk
@author : Rinka
@date   : 2019/9/13
"""
import sys
import os

from app import gdp

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")
from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = gdp.SERVER_KEY
socketio = SocketIO()
socketio.init_app(app)

from .auth import cgi
from .im import cgi

@app.route('/')
def index():
    return "Camptalk Gateway"


@app.route('/push')
def push_once():
    event_name = 'message'
    data = request.values.get("msg")
    from app.basic.std_response import StdResponse
    broadcasted_data = StdResponse(data={"msg": "test broadcast"}).to_json()
    print("publish msg==>", broadcasted_data)
    socketio.emit(event_name, broadcasted_data, broadcast=True)
    return 'send msg successful!'
