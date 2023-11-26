"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.user_dao import UserDAO
from .orders.artist_dao import ArtistDAO
from .orders.album_dao import AlbumDAO
from .orders.label_dao import LabelDAO
from .orders.genre_dao import GenreDAO
from .orders.device_dao import DeviceDAO
from .orders.song_dao import SongDAO
from .orders.playlist_dao import PlaylistDAO
from .orders.artistlabel_dao import ArtistLabelDAO

user_dao = UserDAO()
artist_dao = ArtistDAO()
album_dao = AlbumDAO()
label_dao = LabelDAO()
genre_dao = GenreDAO()
device_dao = DeviceDAO()
song_dao = SongDAO()
playlist_dao = PlaylistDAO()
artistlabel_dao = ArtistLabelDAO()
