class stats:
    def __init__(self):
        self.points = 0
        self.play_time = 0
        self.enemies_destroyed = 0
        self.boss_defeated = 0
        self.shots = 0
        self.shots_hit = 0
    def load_best_stats(self):
        with open("best_stats.txt", "r") as f:
            lines = f.readlines()

            self.points = int(lines[0])
            self.play_time = int(lines[1])
            self.enemies_destroyed = int(lines[2])
            self.boss_defeated = int(lines[3])
            self.shots = int(lines[4])
            self.shots_hit = int(lines[5])
    def save_best(self):
        print(self.boss_defeated)
        with open("best_stats.txt", "w") as f:
            f.write(f"{self.points}\n")
            f.write(f"{self.play_time}\n")
            f.write(f"{self.enemies_destroyed}\n")
            f.write(f"{self.boss_defeated}\n")
            f.write(f"{self.shots}\n")
            f.write(f"{self.shots_hit}\n")
    def copy_from(self, other):
        self.points = other.points
        self.play_time = other.play_time
        self.enemies_destroyed = other.enemies_destroyed
        self.boss_defeated = other.boss_defeated
        self.shots = other.shots
        self.shots_hit = other.shots_hit
