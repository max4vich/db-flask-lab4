"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import listeninghistory_controller
from t08_flask_mysql.app.my_project.auth.domain import ListeningHistory

listeninghistories_bp = Blueprint('listeninghistories', __name__, url_prefix='/listeninghistories')


@listeninghistories_bp.get('')
def get_all_listeninghistories() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(listeninghistory_controller.find_all()), HTTPStatus.OK)


@listeninghistories_bp.post('')
def create_listeninghistory() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    listeninghistories = ListeningHistory.create_from_dto(content)
    listeninghistory_controller.create(listeninghistories)
    return make_response(jsonify(listeninghistories.put_into_dto()), HTTPStatus.CREATED)