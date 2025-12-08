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
        jolts = ""
        for i in range(11):
            jolt = max(line[:i - 11])
            line = line[line.index(jolt) + 1:]
            jolts += jolt
        jolts += max(line)
        return int(jolts)

if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
