"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import playlist_controller
from t08_flask_mysql.app.my_project.auth.domain import Playlist

playlist_bp = Blueprint('playlists', __name__, url_prefix='/playlists')


@playlist_bp.get('')
def get_all_playlists() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(playlist_controller.find_all()), HTTPStatus.OK)


@playlist_bp.post('')
def create_playlist() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    playlist = Playlist.create_from_dto(content)
    playlist_controller.create(playlist)
    return make_response(jsonify(playlist.put_into_dto()), HTTPStatus.CREATED)


@playlist_bp.get('/<int:playlist_id>')
def get_playlist(playlist_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(playlist_controller.find_by_id(playlist_id)), HTTPStatus.OK)


@playlist_bp.put('/<int:playlist_id>')
def update_playlist(playlist_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    playlist = Playlist.create_from_dto(content)
    playlist_controller.update(playlist_id, playlist)
    return make_response("Genre updated", HTTPStatus.OK)


@playlist_bp.patch('/<int:playlist_id>')
def patch_playlist(playlist_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    playlist_controller.patch(playlist_id, content)
    return make_response("Genre updated", HTTPStatus.OK)


@playlist_bp.delete('/<int:playlist_id>')
def delete_playlist(playlist_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    playlist_controller.delete(playlist_id)
    return make_response("Genre deleted", HTTPStatus.OK)
