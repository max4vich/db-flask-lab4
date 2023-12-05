"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy import text

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Artist


class ArtistDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Artist

    @classmethod
    def insert_rows_into_artists(cls) -> None:
        """
        Inserts 10 rows into the artist table.
        """
        try:
            # Using SQLAlchemy's text() function to execute a raw SQL query
            query = text("""INSERT INTO artist (name) VALUES (:artist_name)""")

            # Execute the query 10 times with different values
            for i in range(1, 11):
                artist_name = f"Noname{i}"
                db.session.execute(query, {"artist_name": artist_name})

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
