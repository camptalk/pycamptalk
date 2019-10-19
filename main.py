# -*- coding: UTF-8 -*-
"""
Project Camptalk
@author : Rinka
@date   : 2019/10/19
"""
from app.application import socketio, app

if __name__ == '__main__':
    print("http://127.0.0.1:11551")
    socketio.run(app, host='0.0.0.0', port=11551, debug=True, log_output=True)
