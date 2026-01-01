from stats import stats

class record:
    def __init__(self):
        self.total_points = 0
        self.total_play_time = 0
        self.total_games = 0
        self.total_win_games = 0
        self.total_enemies_destroyed = 0
        self.total_boss_defeated = 0
        self.total_shots = 0
        self.total_shots_hit = 0
    def load_records(self):
        with open("general_records.txt", "r") as f:
            lines = f.readlines()

            self.total_points = int(lines[0])
            self.total_play_time = int(lines[1])
            self.total_games = int(lines[2])
            self.total_win_games = int(lines[3])
            self.total_enemies_destroyed = int(lines[4])
            self.total_boss_defeated = int(lines[5])
            self.total_shots = int(lines[6])
            self.total_shots_hit = int(lines[7])
    def save_records(self):
        with open("general_records.txt", "w") as f:
            f.write(f"{self.total_points}\n")
            f.write(f"{self.total_play_time}\n")
            f.write(f"{self.total_games}\n")
            f.write(f"{self.total_win_games}\n")
            f.write(f"{self.total_enemies_destroyed}\n")
            f.write(f"{self.total_boss_defeated}\n")
            f.write(f"{self.total_shots}\n")
            f.write(f"{self.total_shots_hit}\n")
    def update(self, game_stats):
        self.total_points += game_stats.points
        self.total_enemies_destroyed += game_stats.enemies_destroyed
        self.total_boss_defeated += game_stats.boss_defeated
        self.total_play_time += game_stats.play_time
        self.total_games += 1
        self.total_shots += game_stats.shots
        self.total_shots_hit += game_stats.shots_hit
        self.total_win_games += game_stats.boss_defeated