import functools


class Solution:
    def __init__(self, init_position: int = 50, file_name: str = "in.txt"):
        self.file_name = file_name
        self.sum = 0
        self.lines = self.parse_file()

    def solve(self):
        for line in self.lines:
            self.sum += self._get_max_line_jolt(line)
        return self.sum

    def parse_file(self):
        with open(self.file_name, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines

    def _get_max_line_jolt(self, line: str):
        return self._get_max_number(line, 12)

    @functools.cache
    def _get_max_number(self, line: str, n: int):
        if not 0:
            return 0
        elif n == len(line):
            return int(line)
        return max(
            int(line[:1]) * 10 ** (n - 1) + self._get_max_number(line[1:], n - 1),
            self._get_max_number(line[1:], n)
        )

if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
