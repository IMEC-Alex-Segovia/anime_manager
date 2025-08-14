import tkinter as tk
from tkinter import ttk

class MainForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Listado de Anime")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.rate_list = ["Todos"]
        self.genre_list = ["Todos"]
        self.state_list = ["Todos"]
        self.columns = ("title", "chapters", "rate", "genre", "state")

        self._setup_ui()
    
    def _setup_ui(self):
        # === TITLE ===
        self.title_label = ttk.Label(self.root, text="Listado de Anime")
        self.title_label.pack(pady=5)
        # === SEARCH ===
        self.search_frame = ttk.Frame(self.root)
        self.search_frame.pack(pady=5)
        self.search_label = ttk.Label(self.search_frame, text="Anime:")
        self.search_label.pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame, width=60)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar")
        self.search_button.pack(side=tk.LEFT, padx=5)
        # === FILTERS ===
        self.filter_frame = ttk.Frame(self.root)
        self.filter_frame.pack(pady=5)
        self.rate_label = ttk.Label(self.filter_frame, text="Calificación:")
        self.rate_label.pack(side=tk.LEFT, padx=5)
        self.rate_cmbx = ttk.Combobox(self.filter_frame, values=self.rate_list, state="readonly", width=15)
        self.rate_cmbx.current(0)
        self.rate_cmbx.pack(side=tk.LEFT, padx=5)
        self.genre_label = ttk.Label(self.filter_frame, text="Género:")
        self.genre_label.pack(side=tk.LEFT, padx=5)
        self.genre_cmbx = ttk.Combobox(self.filter_frame, values=self.genre_list, state="readonly", width=15)
        self.genre_cmbx.current(0)
        self.genre_cmbx.pack(side=tk.LEFT, padx=5)
        self.state_label = ttk.Label(self.filter_frame, text="Estado:")
        self.state_label.pack(side=tk.LEFT, padx=5)
        self.state_cmbx = ttk.Combobox(self.filter_frame, values=self.state_list, state="readonly", width=15)
        self.state_cmbx.current(0)
        self.state_cmbx.pack(side=tk.LEFT, padx=5)
        self.filter_button = ttk.Button(self.filter_frame, text="Filtrar:")
        self.filter_button.pack(side=tk.LEFT, padx=5)
        # === ANIME LIST ===
        self.anime_list_frame = ttk.Frame(self.root)
        self.anime_list_frame.pack(pady=5)
        self.anime_list_tree = ttk.Treeview(self.anime_list_frame, columns=self.columns, show="headings", height=15)
        self.anime_list_tree.pack()
        self.anime_list_tree.heading(self.columns[0], text="Título")
        self.anime_list_tree.heading(self.columns[1], text="Episodios")
        self.anime_list_tree.heading(self.columns[2], text="Calificación")
        self.anime_list_tree.heading(self.columns[3], text="Género")
        self.anime_list_tree.heading(self.columns[4], text="Estado")
        self.anime_list_tree.column(self.columns[0], width=280)
        self.anime_list_tree.column(self.columns[1], width=70)
        self.anime_list_tree.column(self.columns[2], width=100)
        self.anime_list_tree.column(self.columns[3], width=100)
        self.anime_list_tree.column(self.columns[4], width=100)
        # === BUTTONS ===
        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.pack(pady=5)
        self.add_button = ttk.Button(self.buttons_frame, text="Agregar")
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.remove_button = ttk.Button(self.buttons_frame, text="Eliminar")
        self.remove_button.pack(side=tk.LEFT, padx=10)
        self.edit_button = ttk.Button(self.buttons_frame, text="Editar")
        self.edit_button.pack(side=tk.LEFT, padx=10)
        self.time_button = ttk.Button(self.buttons_frame, text="Tiempo invertido")
        self.time_button.pack(side=tk.LEFT, padx=10)

    def boot(self):
        self.root.mainloop()