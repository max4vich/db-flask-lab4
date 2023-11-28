"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Song(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45))
    duration = db.Column(db.Time)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))

    song_genres = db.relationship('SongGenre', backref='song')
    listening_histories = db.relationship('ListeningHistory', backref='song')
    current_listenings = db.relationship('CurrentListening', backref='song')
    playlist_songs = db.relationship('PlaylistSong', backref='song')

    def __repr__(self) -> str:
        return f"Song({self.id}, '{self.title}', '{self.duration}', '{self.album_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        song_genres_list = [song_genres.put_into_dto() for song_genres in self.song_genres]
        listening_histories_list = [listening_histories.put_into_dto() for listening_histories in self.listening_histories]
        current_listenings_list = [current_listenings.put_into_dto() for current_listenings in self.current_listenings]
        playlist_songs_list = [playlist_songs.put_into_dto() for playlist_songs in self.playlist_songs]
        return {
            "id": self.id,
            "title": self.title,
            "duration": self.duration.strftime("%H:%M:%S"),
            "album_id": self.album_id,
            "album_name": self.album.title,
            "song_genres_list": song_genres_list,
            "listening_histories_list": listening_histories_list,
            "current_listenings_list": current_listenings_list,
            "playlist_songs_list": playlist_songs_list
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Song:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Song(
            title=dto_dict.get("title"),
            duration=dto_dict.get("duration"),
            album_id=dto_dict.get("album_id"),
        )
        return obj
