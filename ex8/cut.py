import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--delimiter", default="\t")
parser.add_argument("input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--fields", nargs="+")
group.add_argument("-c", "--characters", nargs="+")

args = parser.parse_args()

stuff_to_cut = None

if args.fields:
    stuff_to_cut = "fields"
    required_fields = list(map(lambda num: int(num) - 1, args.fields))
elif args.characters:
    stuff_to_cut = "chars"
    required_fields = list(map(lambda num: int(num) - 1, args.characters))

output_lines = []


def process_line(line: str) -> str:
    if stuff_to_cut == "fields":
        stripped_line = line.rstrip().split(args.delimiter)
        stripped_line = stripped_line[required_fields[0] : required_fields[1] + 1]
        stripped_line = args.delimiter.join(stripped_line)
    elif stuff_to_cut == "chars":
        stripped_line = line[required_fields[0] : required_fields[1] + 1]

    return stripped_line


whole_file = args.input.readlines()
for line in whole_file:
    processed_line = process_line(line)
    output_lines.append(processed_line)

for line in output_lines:
    print(line)
