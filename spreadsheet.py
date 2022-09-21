import sys
import csv
from typing import List


def read_csv_from_file(path: str) -> List:
    output = []
    with open(path, newline="", encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader) # skip the headers
        for row in reader:
            output.append(row)
    return output


def main(args: List):
    if len(args) == 2:
        read_csv_from_file(args[1])


if __name__ == "__main__":
    main(sys.argv)