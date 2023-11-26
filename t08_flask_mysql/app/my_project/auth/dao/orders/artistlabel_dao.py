"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import ArtistLabel


class ArtistLabelDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = ArtistLabel
