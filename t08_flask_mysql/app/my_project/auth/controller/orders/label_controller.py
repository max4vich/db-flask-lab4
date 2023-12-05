"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from flask import Response, request, make_response, jsonify
from flask_restx._http import HTTPStatus

from t08_flask_mysql.app.my_project.auth.domain.orders.label import Label
from t08_flask_mysql.app.my_project.auth.service import label_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class LabelController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = label_service

    @classmethod
    def create_label(cls, name: str, country: str) -> Label:
        """
        Creates a new label.
        :param name: Label name
        :param country: Label country
        :return: Created Label object
        """
        return cls._service.create_label(name, country)
