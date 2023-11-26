"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.user_route import user_bp
    from .orders.artist_route import artist_bp
    from .orders.album_route import album_bp
    from .orders.label_route import label_bp
    from .orders.genre_route import genre_bp
    from .orders.device_route import device_bp
    from .orders.song_route import song_bp
    from .orders.playlist_route import playlist_bp
    from .orders.artistlabel_route import artistlabel_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(artist_bp)
    app.register_blueprint(album_bp)
    app.register_blueprint(label_bp)
    app.register_blueprint(genre_bp)
    app.register_blueprint(device_bp)
    app.register_blueprint(song_bp)
    app.register_blueprint(playlist_bp)
    app.register_blueprint(artistlabel_bp)
