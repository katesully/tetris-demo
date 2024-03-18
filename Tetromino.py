import time


class Tetromino:
    def __init__(self, shape):
        self.shape = shape


class TetrominoFactory:
    def create_tetromino(self, shape):
        pass


class FreezePowerupTetrominoFactory(TetrominoFactory):
    def create_tetromino(self, shape, slow_duration):
        return FreezePowerupTetromino(shape, slow_duration)


class BombBlockTetrominoFactory(TetrominoFactory):
    def create_tetromino(self, shape):
        return BombBlockTetromino(shape)


class FreezePowerupTetromino(Tetromino):
    def __init__(self):
        # super().__init__(shape)
        self.slow_duration = 5

    def freeze(self):
        time.sleep(self.slow_duration)


class BombBlockTetromino(Tetromino):
    def __init__(self, shape, explosion_pattern, explosion_range):
        super().__init__(shape)
        self.explosion_pattern = explosion_pattern
        self.explosion_range = explosion_range

    def trigger_explosion(self):
        print(
            "Triggering explosion with pattern {} and range {}".format(
                self.explosion_pattern, self.explosion_range
            )
        )
