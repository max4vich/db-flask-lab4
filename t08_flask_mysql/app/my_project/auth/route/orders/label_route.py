"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import label_controller
from t08_flask_mysql.app.my_project.auth.domain import Label

label_bp = Blueprint('labels', __name__, url_prefix='/labels')


@label_bp.get('')
def get_all_labels() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(label_controller.find_all()), HTTPStatus.OK)


@label_bp.post('')
def create_label() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    label = Label.create_from_dto(content)
    label_controller.create(label)
    return make_response(jsonify(label.put_into_dto()), HTTPStatus.CREATED)


@label_bp.get('/<int:label_id>')
def get_label(label_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(label_controller.find_by_id(label_id)), HTTPStatus.OK)


@label_bp.put('/<int:label_id>')
def update_label(label_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    label = Label.create_from_dto(content)
    label_controller.update(label_id, label)
    return make_response("Label updated", HTTPStatus.OK)


@label_bp.patch('/<int:label_id>')
def patch_label(label_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    label_controller.patch(label_id, content)
    return make_response("Label updated", HTTPStatus.OK)


@label_bp.delete('/<int:label_id>')
def delete_label(label_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    label_controller.delete(label_id)
    return make_response("Label deleted", HTTPStatus.OK)
