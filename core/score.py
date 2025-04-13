class ScoreManager:
    def __init__(self):
        self.score = 0
        self.successes = 0
        self.failures = 0

    def add_points(self, amount):
        self.score += amount
        self.successes += 1

    def fail(self):
        self.failures += 1

    def get_score(self):
        return self.score

    def get_summary(self):
        return f"Score: {self.score} | Réussites: {self.successes} | Échecs: {self.failures}"

# Singleton
score = ScoreManager()
