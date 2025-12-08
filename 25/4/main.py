class Solution:
    LIMIT = 4

    def __init__(self, init_position: int = 50, file_name: str = "in.txt"):
        self.file_name = file_name
        self.lines = self.parse_file()
        self.grid = self.parse_grid()
        self.sum = 0
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def solve(self):
        while True:
            sum_before = self.sum
            indices_to_clear = []
            for y in range(self.height):
                for x in range(self.width):
                    if self.grid[y][x] == 1 and (no_rolls := self._is_possible_roll(x, y)):
                        self.sum += no_rolls
                        indices_to_clear.append((y, x))
            for y, x in indices_to_clear:
                self.grid[y][x] = 0
            if sum_before == self.sum:
                break
        return self.sum

    def _is_possible_roll(self, x, y):
        combinations = self._get_8_combinations(x, y)
        return sum(self.grid[y + dy][x + dx] for dy, dx in combinations) < self.LIMIT

    def _get_8_combinations(self, x, y):
        return [
            (dy, dx)
            for dy in (-1, 0, 1)
            for dx in (-1, 0, 1)
            if not (dx == 0 and dy == 0)
            if 0 <= x + dx < self.width and 0 <= y + dy < self.height
        ]
    
    def parse_file(self):
        with open(self.file_name, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines

    def parse_grid(self):
        grid = []
        for line in self.lines:
            line = [1 if char == "@" else 0 for char in line]
            grid.append(line)
        return grid

if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
