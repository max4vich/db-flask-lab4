"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import device_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class DeviceService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = device_dao
