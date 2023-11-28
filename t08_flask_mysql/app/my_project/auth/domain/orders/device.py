"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Device(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "device"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    device_type = db.Column(db.String(45))

    user_devices = db.relationship('UserDevice', backref='device')
    current_listening_devices = db.relationship('CurrentListeningDevice', backref='currentlistening')

    def __repr__(self) -> str:
        return f"Device({self.id}, '{self.name}', '{self.device_type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        user_devices_list = [user_devices.put_into_dto() for user_devices in self.user_devices]
        current_listening_devices_list = [current_listening_devices.put_into_dto() for current_listening_devices in self.current_listening_devices]
        return {
            "id": self.id,
            "name": self.name,
            "device_type": self.device_type,
            "user_devices_list": user_devices_list,
            "current_listening_devices_list": current_listening_devices_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Device:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Device(
            name=dto_dict.get("name"),
            device_type=dto_dict.get("device_type")
        )
        return obj
