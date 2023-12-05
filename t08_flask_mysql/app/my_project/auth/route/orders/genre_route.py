"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import genre_controller
from t08_flask_mysql.app.my_project.auth.domain import Genre

genre_bp = Blueprint('genres', __name__, url_prefix='/genres')


@genre_bp.get('')
def get_all_genres() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(genre_controller.find_all()), HTTPStatus.OK)


@genre_bp.post('')
def create_genre() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    genre = Genre.create_from_dto(content)
    genre_controller.create(genre)
    return make_response(jsonify(genre.put_into_dto()), HTTPStatus.CREATED)


@genre_bp.get('/<int:genre_id>')
def get_genre(genre_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(genre_controller.find_by_id(genre_id)), HTTPStatus.OK)


@genre_bp.put('/<int:genre_id>')
def update_genre(genre_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    genre = Genre.create_from_dto(content)
    genre_controller.update(genre_id, genre)
    return make_response("Genre updated", HTTPStatus.OK)


@genre_bp.patch('/<int:genre_id>')
def patch_genre(genre_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    genre_controller.patch(genre_id, content)
    return make_response("Genre updated", HTTPStatus.OK)


@genre_bp.delete('/<int:genre_id>')
def delete_genre(genre_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    genre_controller.delete(genre_id)
    return make_response("Genre deleted", HTTPStatus.OK)
