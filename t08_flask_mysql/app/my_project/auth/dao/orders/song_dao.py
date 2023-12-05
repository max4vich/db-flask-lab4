"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy.sql import func
from datetime import time

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Song


class SongDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Song

    @classmethod
    def get_max_duration(cls) -> time:
        """
        Retrieve the maximum duration from the 'song' table.
        :return: Maximum duration
        """
        max_duration = db.session.query(func.max(Song.duration)).scalar()
        return max_duration