"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import artist_controller
from t08_flask_mysql.app.my_project.auth.domain import Artist
from t08_flask_mysql.app.my_project.auth.dao import artist_dao

artist_bp = Blueprint('artists', __name__, url_prefix='/artists')


@artist_bp.route('/insert-rows-into-artists', methods=['POST'])
def insert_rows_into_artists():
    try:
        artist_dao.insert_rows_into_artists()
        return make_response(jsonify({"message": "Rows inserted successfully"}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)



@artist_bp.get('')
def get_all_artists() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(artist_controller.find_all()), HTTPStatus.OK)


@artist_bp.post('')
def create_artist() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    artist = Artist.create_from_dto(content)
    artist_controller.create(artist)
    return make_response(jsonify(artist.put_into_dto()), HTTPStatus.CREATED)


@artist_bp.get('/<int:artist_id>')
def get_user(artist_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(artist_controller.find_by_id(artist_id)), HTTPStatus.OK)


@artist_bp.put('/<int:artist_id>')
def update_user(artist_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    artist = Artist.create_from_dto(content)
    artist_controller.update(artist_id, artist)
    return make_response("Artist updated", HTTPStatus.OK)


@artist_bp.patch('/<int:artist_id>')
def patch_user(artist_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    artist_controller.patch(artist_id, content)
    return make_response("Artist updated", HTTPStatus.OK)


@artist_bp.delete('/<int:artist_id>')
def delete_user(artist_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    artist_controller.delete(artist_id)
    return make_response("Artist deleted", HTTPStatus.OK)
