import tkinter as tk
from tkinter import ttk

class MainForm:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Listado de Anime")
        self.root.geometry("850x500")
        self.root.resizable(False, False)

        self.SEARCH_ENTRY_WIDTH = 108

        self.RATE_CMBX_LIST = ["Todos"]
        self.GENRE_CMBX_LIST = ["Todos"]
        self.STATE_CMBX_LIST = ["Todos"]
        self.TYPE_CMBX_LIST = ["Todos"]
        self.COLUMNS = ("title", "chapters", "rate", "genre", "state")
    
    def _setup_ui(self):
        # === TITLE ===
        self.title_label = ttk.Label(self.root, text="Listado de Anime")
        self.title_label.pack(pady=5)
        # === SEARCH ===
        self.search_frame = ttk.Frame(self.root)
        self.search_frame.pack(pady=5)
        self.search_label = ttk.Label(self.search_frame, text="Título:")
        self.search_label.pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame, width=self.SEARCH_ENTRY_WIDTH)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar")
        self.search_button.pack(side=tk.LEFT, padx=5)
        # === FILTERS ===
        self.filter_frame = ttk.Frame(self.root)
        self.filter_frame.pack(pady=5)
        self.rate_label = ttk.Label(self.filter_frame, text="Calificación:")
        self.rate_label.pack(side=tk.LEFT, padx=5)
        self.rate_cmbx = ttk.Combobox(self.filter_frame, values=self.RATE_CMBX_LIST, state="readonly", width=15)
        self.rate_cmbx.current(0)
        self.rate_cmbx.pack(side=tk.LEFT, padx=5)
        self.genre_label = ttk.Label(self.filter_frame, text="Género:")
        self.genre_label.pack(side=tk.LEFT, padx=5)
        self.genre_cmbx = ttk.Combobox(self.filter_frame, values=self.GENRE_CMBX_LIST, state="readonly", width=15)
        self.genre_cmbx.current(0)
        self.genre_cmbx.pack(side=tk.LEFT, padx=5)
        self.state_label = ttk.Label(self.filter_frame, text="Estado:")
        self.state_label.pack(side=tk.LEFT, padx=5)
        self.state_cmbx = ttk.Combobox(self.filter_frame, values=self.STATE_CMBX_LIST, state="readonly", width=15)
        self.state_cmbx.current(0)
        self.state_cmbx.pack(side=tk.LEFT, padx=5)
        self.type_label = ttk.Label(self.filter_frame, text="Tipo:")
        self.type_label.pack(side=tk.LEFT, padx=5)
        self.type_cmbx = ttk.Combobox(self.filter_frame, values=self.TYPE_CMBX_LIST, state="readonly", width=15)
        self.type_cmbx.current(0)
        self.type_cmbx.pack(side=tk.LEFT, padx=5)
        self.filter_button = ttk.Button(self.filter_frame, text="Filtrar")
        self.filter_button.pack(side=tk.LEFT, padx=5)
        # === ANIME LIST ===
        self.anime_list_frame = ttk.Frame(self.root)
        self.anime_list_frame.pack(pady=5)
        self.anime_list_tree = ttk.Treeview(self.anime_list_frame, columns=self.COLUMNS, show="headings", height=15)
        self.anime_list_tree.pack()
        self.anime_list_tree.heading(self.COLUMNS[0], text="Título")
        self.anime_list_tree.heading(self.COLUMNS[1], text="Episodios")
        self.anime_list_tree.heading(self.COLUMNS[2], text="Calificación")
        self.anime_list_tree.heading(self.COLUMNS[3], text="Género")
        self.anime_list_tree.heading(self.COLUMNS[4], text="Estado")
        self.anime_list_tree.column(self.COLUMNS[0], width=350)
        self.anime_list_tree.column(self.COLUMNS[1], width=90)
        self.anime_list_tree.column(self.COLUMNS[2], width=120)
        self.anime_list_tree.column(self.COLUMNS[3], width=120)
        self.anime_list_tree.column(self.COLUMNS[4], width=120)
        # === BUTTONS ===
        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.pack(pady=5)
        self.add_button = ttk.Button(self.buttons_frame, text="Agregar")
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.remove_button = ttk.Button(self.buttons_frame, text="Eliminar")
        self.remove_button.pack(side=tk.LEFT, padx=10)
        self.edit_button = ttk.Button(self.buttons_frame, text="Editar")
        self.edit_button.pack(side=tk.LEFT, padx=10)
        self.time_button = ttk.Button(self.buttons_frame, text="Tiempo")
        self.time_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        self._setup_ui()
        self.root.mainloop()