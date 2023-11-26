"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import album_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AlbumController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = album_service
