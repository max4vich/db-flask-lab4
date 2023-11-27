"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import currentlisteningdevice_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CurrentListeningDeviceService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = currentlisteningdevice_dao
