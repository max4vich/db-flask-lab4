"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class DeviceInfo(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "device_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer)
    def __repr__(self) -> str:
        return f"DeviceInfo({self.id}, '{self.device_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """

        return {
            "id": self.id,
            "device_id": self.device_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DeviceInfo:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = DeviceInfo(
            id=dto_dict.get("id"),
            device_id=dto_dict.get("device_id")
        )
        return obj
