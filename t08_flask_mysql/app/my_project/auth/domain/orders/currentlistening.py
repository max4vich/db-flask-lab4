"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto

import datetime


class CurrentListening(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "currentlistening"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
    start_time = db.Column(db.DateTime, default=datetime.datetime.now)

    # current_listening_devices = db.relationship('CurrentListeningDevice', backref='currentlistening')

    def __repr__(self) -> str:
        return f"CurrentListening({self.user_id}, '{self.song_id}', '{self.start_time}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        # current_listening_devices_list = [current_listening_devices.put_into_dto() for current_listening_devices in self.current_listening_devices]
        return {
            "user_id": self.user_id,
            "song_id": self.song_id,
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            # "current_listening_devices_list": current_listening_devices_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CurrentListening:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CurrentListening(
            user_id=dto_dict.get("user_id"),
            song_id=dto_dict.get("song_id"),
            start_time=dto_dict.get("start_time")
        )
        return obj
