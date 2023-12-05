"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import songgenre_controller
from t08_flask_mysql.app.my_project.auth.domain import SongGenre

songgenre_bp = Blueprint('songgenres', __name__, url_prefix='/songgenres')


@songgenre_bp.get('')
def get_all_songgenre() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(songgenre_controller.find_all()), HTTPStatus.OK)


@songgenre_bp.post('')
def create_songgenre() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    songgenre = SongGenre.create_from_dto(content)
    songgenre_controller.create(songgenre)
    return make_response(jsonify(songgenre.put_into_dto()), HTTPStatus.CREATED)