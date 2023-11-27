"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import userdevice_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class UserDeviceService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = userdevice_dao
