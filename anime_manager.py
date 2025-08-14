from main_form import MainForm
from pathlib import Path
import os
import sqlite3

class AnimeManager(MainForm):
    def __init__(self):
        super().__init__()
        self.DB_PATH = self.get_db_path()
        self.init_anime_db()
        self.RATE_LIST = ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐", "❓"]
        self.STATE_LIST = ["Viendo", "Terminado", "Por ver", "En pausa"]
        self.GENRE_LIST = ["Acción", "Aventura", "Comedia", "Drama", "Fantasía", "Ciencia Ficción",
            "Romance", "Slice of Life", "Terror", "Misterio", "Thriller", "Supernatural",
            "Deportes", "Musical", "Psicológico", "Mecha", "Harem", "Isekai", "Shounen",
            "Shoujo", "Seinen", "Josei", "Yaoi", "Yuri", "Ecchi", "Hentai" 
        ]
        self.TYPE_LIST = ["Anime", "Película", "OVA"]
        
        self.RATE_CMBX_LIST += self.RATE_LIST
        self.GENRE_CMBX_LIST += self.GENRE_LIST
        self.STATE_CMBX_LIST += self.STATE_LIST
        self.TYPE_CMBX_LIST += self.TYPE_LIST
    
    def get_db_path(self):
        appdata_dir = Path(os.getenv("LOCALAPPDATA", Path.home())) / "Anime Manager App"
        appdata_dir.mkdir(parents=True, exist_ok=True)
        return appdata_dir / "anime_manager_db.db"

    def init_anime_db(self):
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                episodes INTEGER NOT NULL,
                rate TEXT NOT NULL,
                state TEXT NOT NULL,
                episode_duration INTEGER NOT NULL,
                genre TEXT NOT NULL,
                type TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()