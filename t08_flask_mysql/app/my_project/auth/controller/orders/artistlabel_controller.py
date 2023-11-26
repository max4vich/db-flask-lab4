"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import artistlabel_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ArtistLabelController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = artistlabel_service
