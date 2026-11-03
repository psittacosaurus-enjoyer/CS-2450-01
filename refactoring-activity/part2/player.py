class Player:
    def __init__(self, x, y, speed, health, score):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.score = score

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        return f"Player moved to position ({self.x}, {self.y})."

    def jump(self, velocity):
        return f"Player jumps with velocity {velocity}."

    def take_damage(self, amount):
        self.health -= amount
        return f"Player took {amount} damage. Remaining health: {self.health}."

    def add_score(self, points):
        self.score += points
        return f"Player gained {points} points. Total score: {self.score}."
