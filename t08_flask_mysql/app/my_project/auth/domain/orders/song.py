"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Song(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45))
    duration = db.Column(db.Time)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))


    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Song({self.id}, '{self.title}', '{self.duration}', '{self.album_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "title": self.title,
            "duration": self.duration.strftime("%H:%M:%S"),
            "album_id": self.album_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Song:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Song(
            title=dto_dict.get("title"),
            duration=dto_dict.get("duration"),
            album_id=dto_dict.get("album_id")
        )
        return obj
