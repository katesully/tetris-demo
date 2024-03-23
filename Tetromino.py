import time


class Tetromino:
    def __init__(self):
        pass
        
        


class TetrominoFactory:
    def create_tetromino(self):
        pass


class FreezePowerupTetrominoFactory(TetrominoFactory):
    def create_tetromino(self, slow_duration):
        return FreezePowerupTetromino(slow_duration)


class BombBlockTetrominoFactory(TetrominoFactory):
    def create_tetromino(self):
        return BombBlockTetromino()


class FreezePowerupTetromino(Tetromino):
    def __init__(self, slow_duration):
        super().__init__()
        self.slow_duration = slow_duration

    def freeze(self):
        time.sleep(self.slow_duration)


class BombBlockTetromino(Tetromino):
    def __init__(self, explosion_pattern, explosion_range):
        super().__init__()
        self.explosion_pattern = explosion_pattern
        self.explosion_range = explosion_range

    def trigger_explosion(self):
        print(
            "Triggering explosion with pattern {} and range {}".format(
                self.explosion_pattern, self.explosion_range
            )
        )
