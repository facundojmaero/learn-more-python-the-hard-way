import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("regex")
parser.add_argument("files", nargs="+")
parser.add_argument("-n", "--line-number", action="store_true")
parser.add_argument("-c", "--count", action="store_true")

args = parser.parse_args()

regex = re.compile(args.regex)

config = {
    "print_filename": len(args.files) > 1,
    "print_line_number": args.line_number,
    "print_count": args.count,
}

lines_to_print = []


def print_lines():
    for line in lines_to_print:
        print(line)


def record_match(line: str, filename: str, line_num: int) -> None:

    line_to_print = ""

    if config.get("print_filename"):
        line_to_print += f"{filename}:"
    if config.get("print_line_number"):
        line_to_print += f"{line_num}:"
    line_to_print += line
    lines_to_print.append(line_to_print)


for filename in args.files:
    with open(filename, "r") as f:
        line_num = 0
        content = f.readlines()
        for line in content:
            line_num += 1
            result = regex.search(line)
            if result:
                clean_line = line.strip()
                record_match(clean_line, filename, line_num)

print_lines()
