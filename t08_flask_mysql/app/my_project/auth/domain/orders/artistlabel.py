"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class ArtistLabel(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "artistlabel"

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), primary_key=True)
    label_id = db.Column(db.Integer, db.ForeignKey('label.id'), primary_key=True)

    def __repr__(self) -> str:
        return f"ArtistLabel({self.artist_id}, '{self.label_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "artist_id": self.artist_id,
            "label_id": self.label_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ArtistLabel:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ArtistLabel(
            artist_id=dto_dict.get("artist_id"),
            label_id = dto_dict.get("label_id")
        )
        return obj
