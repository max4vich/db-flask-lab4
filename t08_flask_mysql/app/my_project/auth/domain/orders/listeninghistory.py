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


class ListeningHistory(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "listeninghistory"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)
    listening_date_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)

    def __repr__(self) -> str:
        return f"ListeningHistory({self.user_id}, '{self.song_id}', '{self.listening_date_time}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "user_id": self.user_id,
            "song_id": self.song_id,
            "listening_date_time": self.listening_date_time.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ListeningHistory:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ListeningHistory(
            user_id=dto_dict.get("user_id"),
            song_id=dto_dict.get("song_id "),
            listening_date_time=dto_dict.get("listening_date_time")
        )
        return obj
