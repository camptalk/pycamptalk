# -*- coding: UTF-8 -*-
"""
Project Camptalk
@author : Rinka
@date   : 2019/10/19
"""
import logging
import uuid

from flask import request
from flask_socketio import emit

from .socket_auth import verify_auth_key
from .. import gdp
from ..application import socketio
from ..basic.std_response import StdResponse


_logger = logging.getLogger(__name__)


@socketio.on('connect')
def on_connect():
    auth_key = request.values.get("auth_key", default=None)
    if auth_key is not None and verify_auth_key(auth_key):
        _logger.info('Client is connected: ' + str(request.sid))
        resp = StdResponse(data={"token": str(uuid.uuid4())})
        emit('connect_response', resp.to_json())
    else:
        _logger.info('Client connect is refused since bad token: ' + str(request.sid) + ' token: ' + auth_key)
        return False


@socketio.on('disconnect')
def on_disconnect():
    logging.debug("disconnect from Camptalk Master: " + str(request.sid))
