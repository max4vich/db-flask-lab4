"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy.testing import db

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import ArtistLabel
from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.orders.artist import Artist
from t08_flask_mysql.app.my_project.auth.domain.orders.label import Label


class ArtistLabelDAO(GeneralDAO):
    _domain_type = ArtistLabel

    @classmethod
    def insert_into_artist_label(cls, artist_name: str, label_name: str) -> None:
        """
        Inserts a record into the ArtistLabel table based on artist and label names.
        :param artist_name: Name of the artist
        :param label_name: Name of the label
        """
        artist = Artist.query.filter_by(name=artist_name).first()
        label = Label.query.filter_by(name=label_name).first()

        if artist is not None and label is not None:
            artist_label = ArtistLabel(artist_id=artist.id, label_id=label.id)
            db.session.add(artist_label)
            db.session.commit()
        else:
            raise ValueError("Artist or Label does not exist")
