"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Album(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "album"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

    songs = db.relationship('Song', backref='album')

    def __repr__(self) -> str:
        return f"Album({self.id}, '{self.title}', {self.artist_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        songs_list = [songs.put_into_dto() for songs in self.songs]
        return {
            "id": self.id,
            "title": self.title,
            "artist_id": self.artist_id,
            "songs_list": songs_list
            # "artist_info": {
            #                 "id": self.artist.id,
            #                 "name": self.artist.name,
            #                 "nick": self.artist.nick
            #             },
            # "songs_list": [song.put_into_dto() for song in self.songs]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Album:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Album(
            title=dto_dict.get("title"),
            artist_id = dto_dict.get("artist_id"),
        )
        return obj
