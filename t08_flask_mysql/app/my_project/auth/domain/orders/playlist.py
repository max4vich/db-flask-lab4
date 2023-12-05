"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Playlist(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "playlist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    playlist_songs = db.relationship('PlaylistSong', backref='playlist')

    def __repr__(self) -> str:
        return f"Playlist({self.id}, '{self.name}', {self.user_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        playlist_songs_list = [playlist_songs.put_into_dto() for playlist_songs in self.playlist_songs]
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "playlist_songs_list": playlist_songs_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Playlist:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Playlist(
            name=dto_dict.get("name"),
            user_id = dto_dict.get("user_id")
        )
        return obj
