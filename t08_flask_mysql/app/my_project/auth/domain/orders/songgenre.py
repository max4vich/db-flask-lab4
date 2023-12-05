"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class SongGenre(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "songgenre"

    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)

    def __repr__(self) -> str:
        return f"SongGenre({self.song_id}, '{self.genre_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "song_id": self.song_id,
            "genre_id": self.genre_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SongGenre:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SongGenre(
            song_id=dto_dict.get("song_id"),
            genre_id = dto_dict.get("genre_id")
        )
        return obj
