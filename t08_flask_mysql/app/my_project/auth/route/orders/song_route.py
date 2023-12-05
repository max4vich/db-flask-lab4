"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus
from flask import json
from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import song_controller
from t08_flask_mysql.app.my_project.auth.dao import song_dao
from t08_flask_mysql.app.my_project.auth.domain import Song

song_bp = Blueprint('songs', __name__, url_prefix='/songs')


@song_bp.get('/max_duration')
def get_max_duration() -> Response:
    """
    Gets the maximum duration of songs.
    :return: Response object
    """
    max_duration = song_dao.get_max_duration()
    max_duration_str = max_duration.strftime("%H:%M:%S")  # Convert time to string
    return make_response(jsonify({"max_duration": max_duration_str}), HTTPStatus.OK)
@song_bp.get('')
def get_all_songs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(song_controller.find_all()), HTTPStatus.OK)


@song_bp.post('')
def create_song() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    song = Song.create_from_dto(content)
    song_controller.create(song)
    return make_response(jsonify(song.put_into_dto()), HTTPStatus.CREATED)


@song_bp.get('/<int:song_id>')
def get_song(song_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(song_controller.find_by_id(song_id)), HTTPStatus.OK)


@song_bp.put('/<int:song_id>')
def update_song(song_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    song = Song.create_from_dto(content)
    song_controller.update(song_id, song)
    return make_response("Song updated", HTTPStatus.OK)


@song_bp.patch('/<int:song_id>')
def patch_song(song_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    song_controller.patch(song_id, content)
    return make_response("Song updated", HTTPStatus.OK)


@song_bp.delete('/<int:song_id>')
def delete_song(song_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    song_controller.delete(song_id)
    return make_response("Song deleted", HTTPStatus.OK)
