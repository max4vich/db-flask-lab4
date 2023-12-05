"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Artist(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "artist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45))
    nick = db.Column(db.String(45))

    artist_labels = db.relationship('ArtistLabel', backref='artist')
    albums = db.relationship('Album', backref='artist')

    def __repr__(self) -> str:
        return f"Artist({self.id}, '{self.name}', {self.nick})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        artist_labels_list = [artist_labels.put_into_dto() for artist_labels in self.artist_labels]
        albums_list = [albums.put_into_dto() for albums in self.albums]
        return {
            "id": self.id,
            "name": self.name,
            "nick": self.nick,
            "artist_labels_list": artist_labels_list,
            "albums_list": albums_list
            # "albums_list": [album.put_into_dto() for album in self.albums],
            # "artist_labels_list": [{
            #     "id": artist_label.label.id,
            #     "name": artist_label.label.name,
            #     "country": artist_label.label.country
            # } for artist_label in self.artist_labels]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Artist:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Artist(
            name=dto_dict.get("name"),
            nick = dto_dict.get("nick")
        )
        return obj
