"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.user_service import UserService
from .orders.artist_service import ArtistService
from .orders.album_service import AlbumService
from .orders.label_service import LabelService
from .orders.genre_service import GenreService
from .orders.device_service import DeviceService
from .orders.song_service import SongService
from .orders.playlist_service import PlaylistService
from .orders.artistlabel_service import ArtistLabelService

user_service = UserService()
artist_service = ArtistService()
album_service = AlbumService()
label_service = LabelService()
genre_service = GenreService()
device_service = DeviceService()
song_service = SongService()
playlist_service = PlaylistService()
artistlabel_service = ArtistLabelService()

