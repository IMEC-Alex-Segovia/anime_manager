import tkinter as tk
from tkinter import ttk, messagebox
from anime import Anime

class AddAnimeForm(tk.Toplevel):
    def __init__(self, master, on_save_callback, rate_list : list[str], 
                 state_list : list[str], genre_list : list[str], type_list : list[str]):
        super().__init__(master)
        self.title("Agregar Anime")
        self.geometry("350x550")
        self.resizable(False, False)
        self.on_save_callback = on_save_callback
        self.rate_list = rate_list
        self.state_list = state_list
        self.genre_list = genre_list
        self.type_list = type_list
        
        self.grab_set()
        self._setup_ui()
    
    def _setup_ui(self):
        self.entries_dict = {}
        self.combobox_dict = {}
        self.add_form_title_label = tk.Label(self, text="Agregar un nuevo Anime")
        self.add_form_title_label.pack(pady=10)
        self._add_entry("Título:", "title")
        self._add_entry("Episodios vistos:", "episodes")
        self._add_entry("Duración por episodio (minutos):", "episode_duration")
        self._add_combobox("Calificación:", "rate", self.rate_list)
        self._add_combobox("Estado:", "state", self.state_list)
        self._add_combobox("Género", "genre", self.genre_list)
        self._add_combobox("Tipo:", "type", self.type_list)
        self.save_button = ttk.Button(self, text="Agregar", command=self._add_anime)
        self.save_button.pack(pady=20)

    def _add_entry(self, label_text : str, entry_key : str):
        tk.Label(self, text=label_text).pack(anchor="w", padx=20, pady=10)
        entry = tk.Entry(self)
        entry.pack(padx=20, fill="x")
        self.entries_dict[entry_key] = entry
    
    def _add_combobox(self, label_text : str, combobox_key : str, cmbx_values : list, current_index : int = 0):
        tk.Label(self, text=label_text).pack(anchor="w", padx=20, pady=10)
        cmbx = ttk.Combobox(self, values=cmbx_values, state="readonly")
        cmbx.current(current_index)
        cmbx.pack(padx=20, fill="x")
        self.combobox_dict[combobox_key] = cmbx
    
    def _add_anime(self):
        title = self.entries_dict["title"].get().strip()
        episodes = self.entries_dict["episodes"].get().strip()
        episode_duration = self.entries_dict["episode_duration"].get().strip()

        if not title or not episodes.isdigit() or not episode_duration.isdigit():
            messagebox.showerror("Error", "Asegúrate de ingresar datos válidos")
            return

        rate = self.combobox_dict["rate"].get()
        state = self.combobox_dict["state"].get()
        genre = self.combobox_dict["genre"].get()
        type = self.combobox_dict["type"].get()

        new_anime = Anime(title=title, episodes=int(episodes), episode_duration=int(episode_duration),
                          rate=rate, state=state, genre=genre, type=type)
        
        if self.on_save_callback(new_anime):
            messagebox.showinfo("Éxito", f'Anime "{title}" agregado correctamente.')
            self.destroy()
        else:
            messagebox.showerror("Error", "No se ha podido agregar el anime.")