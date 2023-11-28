"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Genre(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "genre"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(255))

    song_genres = db.relationship('SongGenre', backref='genre')
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Genre({self.id}, '{self.name}', '{self.description}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        song_genres_list = [song_genres.put_into_dto() for song_genres in self.song_genres]
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "song_genres_list": song_genres_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Genre:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Genre(
            name=dto_dict.get("name"),
            description=dto_dict.get("description")
        )
        return obj
