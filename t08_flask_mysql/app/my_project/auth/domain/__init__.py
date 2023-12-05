"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
from t08_flask_mysql.app.my_project.auth.domain.orders.user import User
from t08_flask_mysql.app.my_project.auth.domain.orders.artist import Artist
from t08_flask_mysql.app.my_project.auth.domain.orders.album import Album
from t08_flask_mysql.app.my_project.auth.domain.orders.label import Label
from t08_flask_mysql.app.my_project.auth.domain.orders.genre import Genre
from t08_flask_mysql.app.my_project.auth.domain.orders.device import Device
from t08_flask_mysql.app.my_project.auth.domain.orders.song import Song
from t08_flask_mysql.app.my_project.auth.domain.orders.playlist import Playlist
from t08_flask_mysql.app.my_project.auth.domain.orders.artistlabel import ArtistLabel
from t08_flask_mysql.app.my_project.auth.domain.orders.userdevice import UserDevice
from t08_flask_mysql.app.my_project.auth.domain.orders.playlistsong import PlaylistSong
from t08_flask_mysql.app.my_project.auth.domain.orders.songgenre import SongGenre
from t08_flask_mysql.app.my_project.auth.domain.orders.listeninghistory import ListeningHistory
from t08_flask_mysql.app.my_project.auth.domain.orders.currentlistening import CurrentListening
from t08_flask_mysql.app.my_project.auth.domain.orders.currentlisteningdevice import CurrentListeningDevice
from t08_flask_mysql.app.my_project.auth.domain.orders.device_info import DeviceInfo
