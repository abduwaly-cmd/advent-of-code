class Solution:
    def __init__(self, init_position: int = 50, file_name: str = "in.txt"):
        self.zeros = 0
        self.position = init_position
        self.file_name = file_name

    def solve(self):
        lines = self.parse_file()
        for line in lines:
            direction, value = line[:1], int(line[1:])
            self.move(direction, value)
        return self.zeros

    def parse_file(self):
        with open(self.file_name, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines

    def move(self, direction: str, value: int):
        if direction == 'R':
            new_position = self.position + value
            if new_position >= 100:
                self.zeros += new_position // 100
                self.position = new_position % 100
            else:
                self.position = new_position
        elif direction == 'L':
            new_position = self.position - value
            if new_position <= 0:
                self.zeros += abs(new_position) // 100
                self.position = new_position % 100
            else:
                self.position = new_position


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())