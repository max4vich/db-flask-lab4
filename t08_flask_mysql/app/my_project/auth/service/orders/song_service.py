"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import song_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class SongService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = song_dao
