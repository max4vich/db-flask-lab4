"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import album_controller
from t08_flask_mysql.app.my_project.auth.domain import Album

album_bp = Blueprint('albums', __name__, url_prefix='/albums')


@album_bp.get('')
def get_all_albums() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(album_controller.find_all()), HTTPStatus.OK)


@album_bp.post('')
def create_album() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    album = Album.create_from_dto(content)
    album_controller.create(album)
    return make_response(jsonify(album.put_into_dto()), HTTPStatus.CREATED)


@album_bp.get('/<int:album_id>')
def get_album(album_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(album_controller.find_by_id(album_id)), HTTPStatus.OK)


@album_bp.put('/<int:album_id>')
def update_album(album_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    album = Album.create_from_dto(content)
    album_controller.update(album_id, album)
    return make_response("Album updated", HTTPStatus.OK)


@album_bp.patch('/<int:album_id>')
def patch_album(album_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    album_controller.patch(album_id, content)
    return make_response("Album updated", HTTPStatus.OK)


@album_bp.delete('/<int:album_id>')
def delete_album(album_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    album_controller.delete(album_id)
    return make_response("Album deleted", HTTPStatus.OK)
