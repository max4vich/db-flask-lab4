"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45))
    email = db.Column(db.String(45))

    listening_histories = db.relationship('ListeningHistory', backref='user')
    playlists = db.relationship('Playlist', backref='user')
    current_listenings = db.relationship('CurrentListening', backref='user')
    user_devices = db.relationship('UserDevice', backref='user')

    def __repr__(self) -> str:
        return f"User({self.id}, '{self.username}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        listening_histories_list = [listening_histories.put_into_dto() for listening_histories in self.listening_histories]
        playlists_list = [playlists.put_into_dto() for playlists in self.playlists]
        current_listenings_list = [current_listenings.put_into_dto() for current_listenings in self.playlists]
        user_devices_list = [user_devices.put_into_dto() for user_devices in self.user_devices]
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "listening_histories_list": listening_histories_list,
            "playlists_list": playlists_list,
            "current_listenings_list": current_listenings_list,
            "user_devices_list": user_devices_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = User(
            username=dto_dict.get("username"),
            email=dto_dict.get("email")
        )
        return obj
