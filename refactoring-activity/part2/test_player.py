from player import Player

def describe_test_player():
    def the_player_moves_correctly():
        p = Player(x=10, y=20, speed=2, health=100, score=0)
        result = p.move(1, 0)  # Move right
        assert p.x == 12
        assert p.y == 20
        assert result == "Player moved to position (12, 20)."

        result = p.move(0, -1)  # Move up
        assert p.x == 12
        assert p.y == 18
        assert result == "Player moved to position (12, 18)."

    def the_player_jumps_correctly():
        p = Player(x=10, y=20, speed=2, health=100, score=0)
        result = p.jump(velocity=15)
        assert result == "Player jumps with velocity 15."

    def the_player_takes_damage_correctly():
        p = Player(x=10, y=20, speed=2, health=100, score=0)
        result = p.take_damage(20)
        assert p.health == 80
        assert result == "Player took 20 damage. Remaining health: 80."

    def the_score_is_added_correctly():
        p = Player(x=10, y=20, speed=2, health=100, score=0)
        result = p.add_score(50)
        assert p.score == 50
        assert result == "Player gained 50 points. Total score: 50."
