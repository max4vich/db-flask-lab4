"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import user_controller
from t08_flask_mysql.app.my_project.auth.domain import User

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.get('')
def get_all_users() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)


@user_bp.post('')
def create_user() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)


@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)


@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    user_controller.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
