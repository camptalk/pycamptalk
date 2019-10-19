# -*- coding: UTF-8 -*-
"""
Project Camptalk
@author : Rinka
@date   : 2019/10/19
"""
import uuid
from datetime import datetime

from app import gdp


class StdResponse:
    def __init__(self, code: int = 200, message: str = "", data: dict = None):
        self._code = code
        self._message = message
        self._data = dict() if data is None else data

    def to_json(self, data_update: dict = None):
        if data_update is not None:
            self._data.update(data_update)
        return {
            "request_id": str(uuid.uuid4()),
            "code": self._code,
            "server": gdp.SERVER_ID,
            "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "message": self._message,
            "data": self._data
        }
