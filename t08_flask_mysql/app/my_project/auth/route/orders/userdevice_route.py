"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import userdevice_controller
from t08_flask_mysql.app.my_project.auth.domain import UserDevice

userdevice_bp = Blueprint('userdevices', __name__, url_prefix='/userdevices')


@userdevice_bp.get('')
def get_all_userdevices() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(userdevice_controller.find_all()), HTTPStatus.OK)


@userdevice_bp.post('')
def create_userdevice() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    userdevice = UserDevice.create_from_dto(content)
    userdevice_controller.create(userdevice)
    return make_response(jsonify(userdevice.put_into_dto()), HTTPStatus.CREATED)