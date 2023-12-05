"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import currentlisteningdevice_controller
from t08_flask_mysql.app.my_project.auth.domain import CurrentListeningDevice

currentlisteningdevice_bp = Blueprint('currentlisteningdevices', __name__, url_prefix='/currentlisteningdevices')


@currentlisteningdevice_bp.get('')
def get_all_currentlisteningdevices() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(currentlisteningdevice_controller.find_all()), HTTPStatus.OK)


@currentlisteningdevice_bp.post('')
def create_currentlisteningdevices() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    currentlisteningdevice = CurrentListeningDevice.create_from_dto(content)
    currentlisteningdevice_controller.create(currentlisteningdevice)
    return make_response(jsonify(currentlisteningdevice.put_into_dto()), HTTPStatus.CREATED)