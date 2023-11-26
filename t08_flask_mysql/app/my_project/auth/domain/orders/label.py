"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Label(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "label"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    country = db.Column(db.String(45))

    def __repr__(self) -> str:
        return f"Label({self.id}, '{self.name}', {self.country})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Label:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Label(
            name=dto_dict.get("name"),
            country = dto_dict.get("country")
        )
        return obj
