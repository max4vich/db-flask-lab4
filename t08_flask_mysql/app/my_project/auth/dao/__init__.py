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
from .orders.userdevice_dao import UserDeviceDAO
from .orders.playlistsong_dao import PlaylistSongDAO
from .orders.songgenre_dao import SongGenreDAO
from .orders.listeninghistory_dao import ListeningHistoryDAO
from .orders.currentlistening_dao import CurrentListeningDAO
from .orders.currentlisteningdevice_dao import CurrentListeningDeviceDAO
from .orders.device_info_dao import DeviceInfoDAO

user_dao = UserDAO()
artist_dao = ArtistDAO()
album_dao = AlbumDAO()
label_dao = LabelDAO()
genre_dao = GenreDAO()
device_dao = DeviceDAO()
song_dao = SongDAO()
playlist_dao = PlaylistDAO()
artistlabel_dao = ArtistLabelDAO()
userdevice_dao = UserDeviceDAO()
playlistsong_dao = PlaylistSongDAO()
songgenre_dao = SongGenreDAO()
listeninghistory_dao = ListeningHistoryDAO()
currentlistening_dao = CurrentListeningDAO()
currentlisteningdevice_dao = CurrentListeningDeviceDAO()
device_info_dao = DeviceInfoDAO()
