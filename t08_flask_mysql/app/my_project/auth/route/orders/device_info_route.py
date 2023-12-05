"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import device_info_controller
from t08_flask_mysql.app.my_project.auth.domain import DeviceInfo

device_info_bp = Blueprint('devices_info', __name__, url_prefix='/devices_info')


@device_info_bp.get('')
def get_all_devices() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(device_info_controller.find_all()), HTTPStatus.OK)


@device_info_bp.post('')
def create_device() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    device_info = DeviceInfo.create_from_dto(content)
    device_info_controller.create(device_info)
    return make_response(jsonify(device_info.put_into_dto()), HTTPStatus.CREATED)


@device_info_bp.get('/<int:device_info_id>')
def get_device(device_info_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(device_info_controller.find_by_id(device_info_id)), HTTPStatus.OK)


@device_info_bp.put('/<int:device_info_id>')
def update_device(device_info_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    device_info = DeviceInfo.create_from_dto(content)
    device_info_controller.update(device_info_id, device_info)
    return make_response("Device info updated", HTTPStatus.OK)


@device_info_bp.patch('/<int:device_info_id>')
def patch_device(device_info_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    device_info_controller.patch(device_info_id, content)
    return make_response("Device info updated", HTTPStatus.OK)


@device_info_bp.delete('/<int:device_info_id>')
def delete_device(device_info_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    device_info_controller.delete(device_info_id)
    return make_response("Device info deleted", HTTPStatus.OK)
