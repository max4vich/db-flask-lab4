"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class CurrentListeningDevice(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "currentlisteningdevice"

    current_listening_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), primary_key=True)

    def __repr__(self) -> str:
        return f"CurrentListeningDevice({self.current_listening_id}, '{self.device_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "current_listening_id": self.current_listening_id,
            "device_id": self.device_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CurrentListeningDevice:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = CurrentListeningDevice(
            current_listening_id=dto_dict.get("current_listening_id"),
            device_id = dto_dict.get("device_id")
        )
        return obj
