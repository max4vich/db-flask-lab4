"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import artist_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ArtistService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = artist_dao
