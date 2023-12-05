"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import song_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class SongController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = song_service
