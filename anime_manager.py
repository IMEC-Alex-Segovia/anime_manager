from main_form import MainForm
from pathlib import Path
import os
import sqlite3
from anime import Anime
from add_anime_form import AddAnimeForm
from tkinter import messagebox

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
                title TEXT NOT NULL,
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
    
    def get_anime_list(self):
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM anime")
        animes = cursor.fetchall()
        return [
            Anime(
                id=anime[0], title=anime[1], episodes=anime[2], rate=anime[3],
                state=anime[4], episode_duration=anime[5], genre=anime[6], type=[7]
                ) for anime in animes
        ]

    def update_anime_treeview(self):
        for item in self.anime_list_tree.get_children():
            self.anime_list_tree.delete(item)
        for anime in self.get_anime_list():
            self.anime_list_tree.insert("", "end", iid=str(anime.id), values=anime.get_anime_trevieew_data())
    
    def start(self):
        self._setup_ui()
        self.update_anime_treeview()
        self.add_button.configure(command=self.open_add_anime_form)
        self.remove_button.configure(command=self.remove_anime)
        self.time_button.configure(command=self.show_time_watching_anime)
        self.root.mainloop()

    def open_add_anime_form(self):
        AddAnimeForm(self.root, self.add_new_anime, self.RATE_LIST, self.STATE_LIST, self.GENRE_LIST, self.TYPE_LIST)
    
    def add_new_anime(self, anime : Anime):
        try:
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO anime (title, episodes, rate, state, episode_duration, genre, type) VALUES (?, ?, ?, ?, ?, ?, ?)",
                anime.get_anime_sql_data()
            )
            conn.commit()
            conn.close()
            self.update_anime_treeview()
            return True
        except:
            return False
    
    def remove_anime(self):
        selected_anime = self.anime_list_tree.selection()
        if selected_anime:
            confirm = messagebox.askokcancel("Confirmación", "¿Estás seguro de querer borrar este Anime?")
            if not confirm:
                return
            
            anime_id = selected_anime[0]
            conn = sqlite3.connect(self.DB_PATH)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM anime WHERE id = ?", (anime_id,))
            conn.commit()
            conn.close()
            self.update_anime_treeview()
            messagebox.showinfo("Éxito", "Anime borrado exitosamente")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un Anime para borrar")
    
    def get_watched_hours(self):
        conn = sqlite3.connect(self.DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT SUM(episodes * episode_duration) AS watched_hours
            FROM anime
            WHERE state IN ('Terminado', 'Viendo', 'En pausa')
        ''')
        watched_hours = cursor.fetchone()
        return round(watched_hours[0] / 60, 2) if watched_hours[0] else None
     
    def show_time_watching_anime(self):
        watched_hours = self.get_watched_hours()
        if watched_hours is None:
            messagebox.showinfo("Tiempo viendo Anime", "Parece que aun no haz visto Anime")
            return
        message = f"¡Usted ha visto {watched_hours} horas de Anime!"
        if (watched_hours / 24) > 1:
            message += f"\nEso equivale a {round(watched_hours / 24, 2)} días."
        messagebox.showinfo("Tiempo viendo Anime", message)