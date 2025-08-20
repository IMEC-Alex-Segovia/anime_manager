class Anime:
    def __init__(self, title: str, id: int = None, episodes : int = 0, episode_duration: int = 25,
                 rate: str = None, genre : list[str] = None, type : str = None, state : str = None):
        self.title = title
        self.episodes = episodes
        self.episode_duration = episode_duration
        self.rate = rate
        self.state = state
        self.genre = genre
        self.type = type
    
    def get_anime_trevieew_data(self) -> tuple:
        return (self.title, self.episodes, self.rate, self.genre, self.state)