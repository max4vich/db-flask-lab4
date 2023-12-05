"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import artistlabel_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ArtistLabelService(GeneralService):
    _dao = artistlabel_dao

    @classmethod
    def insert_into_artist_label(cls, artist_name: str, label_name: str) -> None:
        """
        Calls the DAO method to insert a record into the ArtistLabel table based on artist and label names.
        :param artist_name: Name of the artist
        :param label_name: Name of the label
        """
        cls._dao.insert_into_artist_label(artist_name, label_name)
