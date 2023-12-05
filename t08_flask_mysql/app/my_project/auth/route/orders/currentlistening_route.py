"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import currentlistening_controller
from t08_flask_mysql.app.my_project.auth.domain import CurrentListening

currentlistening_bp = Blueprint('currentlistenings', __name__, url_prefix='/currentlistenings')


@currentlistening_bp.get('')
def get_all_currentlistenings() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(currentlistening_controller.find_all()), HTTPStatus.OK)


@currentlistening_bp.post('')
def create_currentlistening() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    currentlistening = CurrentListening.create_from_dto(content)
    currentlistening_controller.create(currentlistening)
    return make_response(jsonify(currentlistening.put_into_dto()), HTTPStatus.CREATED)