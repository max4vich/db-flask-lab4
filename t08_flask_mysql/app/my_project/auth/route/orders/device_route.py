"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import device_controller
from t08_flask_mysql.app.my_project.auth.domain import Device

device_bp = Blueprint('devices', __name__, url_prefix='/devices')


@device_bp.get('')
def get_all_devices() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(device_controller.find_all()), HTTPStatus.OK)


@device_bp.post('')
def create_device() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    device = Device.create_from_dto(content)
    device_controller.create(device)
    return make_response(jsonify(device.put_into_dto()), HTTPStatus.CREATED)


@device_bp.get('/<int:device_id>')
def get_device(device_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(device_controller.find_by_id(device_id)), HTTPStatus.OK)


@device_bp.put('/<int:device_id>')
def update_device(device_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    device = Device.create_from_dto(content)
    device_controller.update(device_id, device)
    return make_response("Device updated", HTTPStatus.OK)


@device_bp.patch('/<int:device_id>')
def patch_device(device_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    device_controller.patch(device_id, content)
    return make_response("Device updated", HTTPStatus.OK)


@device_bp.delete('/<int:device_id>')
def delete_device(device_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    device_controller.delete(device_id)
    return make_response("Device deleted", HTTPStatus.OK)
