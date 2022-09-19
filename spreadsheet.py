import sys
import csv
from typing import List


def read_csv(path: str) -> List:
    output = []
    with open(path, encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None) # skip the headers
        for row in reader:
            output.append(row)
    return output


def main(args: List):
    if len(args) == 2:
        read_csv(args[1])


if __name__ == "__main__":
    main(sys.argv)