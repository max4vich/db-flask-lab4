"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class PlaylistSong(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "playlistsong"

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)

    def __repr__(self) -> str:
        return f"PlaylistSong({self.playlist_id}, '{self.song_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "playlist_id": self.playlist_id,
            "song_id": self.song_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PlaylistSong:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = PlaylistSong(
            playlist_id=dto_dict.get("playlist_id"),
            song_id = dto_dict.get("song_id")
        )
        return obj
