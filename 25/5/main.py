class Solution:
    def __init__(self, init_position: int = 50, file_name: str = "in.txt"):
        self.file_name = file_name
        self.lines = self.parse_file()
        self.ranges, _ = self.parse_ranges()
        self.sum = 0

    def solve(self):
        new_ranges = []
        for (min1, max1) in self.ranges:
            if ranges := list(filter(lambda r: min1 <= r[1] and max1 >= r[0], new_ranges)):
                mins = [min1]
                maxs = [max1]
                for data in ranges:
                    existing = new_ranges.index(data)
                    min2, max2 = new_ranges.pop(existing)
                    mins.append(min2)
                    maxs.append(max2)
                new_ranges.append((min(mins), max(maxs)))
            else:
                new_ranges.append((min1, max1))
        return sum(y - x + 1 for (x, y) in new_ranges)

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
