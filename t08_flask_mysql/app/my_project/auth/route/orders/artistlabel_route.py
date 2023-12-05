"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import artistlabel_controller
from t08_flask_mysql.app.my_project.auth.domain import ArtistLabel

artistlabel_bp = Blueprint('artistlabels', __name__, url_prefix='/artistlabels')


@artistlabel_bp.post('/insert-artist-label')
def insert_artist_label() -> Response:
    """
    Inserts a record into the artistlabel table.
    :return: Response object
    """
    content = request.get_json()

    # Extract artist_name and label_name from the request content
    artist_name = content.get("artist_name")
    label_name = content.get("label_name")

    try:
        # Call the controller method to insert into artistlabel
        artistlabel_controller.insert_into_artist_label(artist_name, label_name)

        # Return a success response
        return make_response(jsonify({"message": "Record inserted successfully"}), HTTPStatus.CREATED)
    except ValueError as e:
        # Return an error response if there's an issue
        return make_response(jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST)


@artistlabel_bp.get('')
def get_all_artistlabels() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(artistlabel_controller.find_all()), HTTPStatus.OK)


@artistlabel_bp.post('')
def create_artistlabel() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    artistlabel = ArtistLabel.create_from_dto(content)
    artistlabel_controller.create(artistlabel)
    return make_response(jsonify(artistlabel.put_into_dto()), HTTPStatus.CREATED)
