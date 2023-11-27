"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.service import listeninghistory_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class ListeningHistoryController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = listeninghistory_service
