"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import label_dao
from t08_flask_mysql.app.my_project.auth.domain.orders.label import Label
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class LabelService(GeneralService):
    """
    Realisation of ClientType service.
    """
    _dao = label_dao

    def create_label(self, name: str, country: str) -> Label:
        return self._dao.create_label(name, country)
