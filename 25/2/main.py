class Solution:
    def __init__(self, input_file: str = "in.txt"):
        self.input_file = input_file
        self.ranges = []
        self.parse_input_file()

    def read_input_file(self):
        with open(self.input_file, "r") as file:
            return file.read()
    
    def parse_input_file(self):
        for line in self.read_input_file().split("\n"):
            ranges = line.split(",")
            for range in ranges:
                self.ranges.append(tuple(map(int, range.split("-"))))

    def is_duplicate(self, num: int):
        str_num = str(num)
        l = len(str_num)
        mid = l // 2
        for step in range(mid):
            first_slice = str_num[:step + 1]
            no_of_slices = l // (step + 1)
            if first_slice * no_of_slices == str_num:
                return True
        return False

    def solve(self):
        duplicates = []
        for (min, max) in self.ranges:
            for num in range(min, max + 1):
                if self.is_duplicate(num):
                    duplicates.append(num)
        return sum(duplicates)

if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())