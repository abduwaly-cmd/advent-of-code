class Solution:
    def __init__(self, init_position: int = 50, file_name: str = "in.txt"):
        self.file_name = file_name
        self.lines = self.parse_file()
        self.ranges, _ = self.parse_ranges()
        self.sum = 0

    def solve(self):
        ranges = sorted(self.ranges)
        current = -1
        for (start, end) in ranges:
            if start <= current:
                start = current + 1
            if start <= end:
                self.sum += end - start + 1
            current = max(current, end)
        return self.sum

    def parse_ranges(self):
        ranges = []
        for i, line in enumerate(self.lines):
            if '-' in line:
                ranges.append(tuple(map(int, line.split('-'))))
            else:
                return ranges, set(map(int, self.lines[i + 1:]))
        return ranges, list()

    def parse_file(self):
        with open(self.file_name, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines

if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
