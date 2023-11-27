"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import playlistsong_controller
from t08_flask_mysql.app.my_project.auth.domain import PlaylistSong

playlistsong_bp = Blueprint('playlistsongs', __name__, url_prefix='/playlistsongs')


@playlistsong_bp.get('')
def get_all_playlistsongs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(playlistsong_controller.find_all()), HTTPStatus.OK)


@playlistsong_bp.post('')
def create_playlistsongs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    playlistsong = PlaylistSong.create_from_dto(content)
    playlistsong_controller.create(playlistsong)
    return make_response(jsonify(playlistsong.put_into_dto()), HTTPStatus.CREATED)