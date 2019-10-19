# -*- coding: UTF-8 -*-
"""
Project Camptalk
@author : Rinka
@date   : 2019/10/19
"""
import json

from flask import request
from flask_socketio import emit

from app import gdp
from app.application import socketio
from app.basic.std_response import StdResponse


@socketio.on('msg')
def recv_message(message):
    print('recv(%s): %s' % (request.sid, message))
    resp = StdResponse(data={"echo": message["msg"]})
    emit('message', resp.to_json())
