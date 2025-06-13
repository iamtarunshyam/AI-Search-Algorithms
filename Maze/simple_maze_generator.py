import numpy as np
import random

class MazeGenerator:
    def __init__(self, width=21, height=21):
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.maze = np.ones((self.height, self.width), dtype=int)  # 1 = wall, 0 = path
        self.start = (1, 1)
        self.goal = (self.height - 2, self.width - 2)

    def generate(self):
        def carve(x, y):
            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and self.maze[ny][nx] == 1:
                    self.maze[ny][nx] = 0
                    self.maze[y + dy // 2][x + dx // 2] = 0
                    carve(nx, ny)

        self.maze[self.start[0]][self.start[1]] = 0
        carve(self.start[1], self.start[0])
        self.maze[self.start[0]][self.start[1]] = 2  # Start
        self.maze[self.goal[0]][self.goal[1]] = 3    # Goal
        return self.maze

    def display(self):
        for row in self.maze:
            print(''.join(['S' if cell == 2 else 'G' if cell == 3 else ' ' if cell == 0 else '█' for cell in row]))

if __name__ == "__main__":
    mg = MazeGenerator(21, 21)
    maze = mg.generate()
    mg.display()
