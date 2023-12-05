"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.user_controller import UserController
from .orders.artist_controller import ArtistController
from .orders.album_controller import AlbumController
from .orders.label_controller import LabelController
from .orders.genre_controller import GenreController
from .orders.device_controller import DeviceController
from .orders.song_controller import SongController
from .orders.playlist_controller import PlaylistController
from .orders.artistlabel_controller import ArtistLabelController
from .orders.userdevice_controller import UserDeviceController
from .orders.playlistsong_controller import PlaylistSongController
from .orders.songgenre_controller import SongGenreController
from .orders.listeninghistory_controller import ListeningHistoryController
from .orders.currentlistening_controller import CurrentListeningController
from .orders.currentlisteningdevice_controller import CurrentListeningDeviceController
from .orders.device_info_controller import DeviceInfoController

user_controller = UserController()
artist_controller = ArtistController()
album_controller = AlbumController()
label_controller = LabelController()
genre_controller = GenreController()
device_controller = DeviceController()
song_controller = SongController()
playlist_controller = PlaylistController()
artistlabel_controller = ArtistLabelController()
userdevice_controller = UserDeviceController()
playlistsong_controller = PlaylistSongController()
songgenre_controller = SongGenreController()
listeninghistory_controller = ListeningHistoryController()
currentlistening_controller = CurrentListeningController()
currentlisteningdevice_controller = CurrentListeningDeviceController()
device_info_controller = DeviceInfoController()
