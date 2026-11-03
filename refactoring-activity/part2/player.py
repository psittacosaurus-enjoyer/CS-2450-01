# Unnecessary base class
class CharacterBase:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
        return f"Player moved to position ({self.x}, {self.y})."


# Child class that inherits unnecessarily
class Player(CharacterBase):
    def __init__(self, x, y, speed, health, score):
        super().__init__(x, y, speed)
        self.health = health
        self.score = score

    def jump(self, velocity):
        return f"Player jumps with velocity {velocity}."

    def take_damage(self, amount):
        self.health -= amount
        return f"Player took {amount} damage. Remaining health: {self.health}."

    def add_score(self, points):
        self.score += points
        return f"Player gained {points} points. Total score: {self.score}."
