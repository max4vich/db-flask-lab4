"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import artistlabel_controller
from t08_flask_mysql.app.my_project.auth.domain import ArtistLabel

artistlabel_bp = Blueprint('artistlabels', __name__, url_prefix='/artistlabels')


@artistlabel_bp.get('')
def get_all_artistlabels() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(artistlabel_controller.find_all()), HTTPStatus.OK)


@artistlabel_bp.post('')
def create_artistlabel() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    artistlabel = ArtistLabel.create_from_dto(content)
    artistlabel_controller.create(artistlabel)
    return make_response(jsonify(artistlabel.put_into_dto()), HTTPStatus.CREATED)