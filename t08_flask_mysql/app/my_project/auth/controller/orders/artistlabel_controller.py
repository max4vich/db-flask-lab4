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

    @classmethod
    def insert_into_artist_label(cls, artist_name: str, label_name: str) -> None:
        """
        Inserts a record into the artistlabel table.
        :param artist_name: Name of the artist
        :param label_name: Name of the label
        """
        cls._service.insert_into_artist_label(artist_name, label_name)
