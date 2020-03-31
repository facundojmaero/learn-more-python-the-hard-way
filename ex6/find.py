import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('location', nargs='?', default='.')
parser.add_argument('-name', type=str, default='*')
parser.add_argument('-type', choices=['d', 'f'], default='all')
parser.add_argument('-exec', type=str, nargs='?', default='echo')

args = parser.parse_args()

# print(args)

p = Path(args.location)


def get_dirs(path, pattern):
    items = []
    for item in path.rglob(pattern):
        if item.is_dir():
            items.append(item)
    return items


def get_files(path, pattern):
    items = []
    for item in path.rglob(pattern):
        if item.is_file():
            items.append(item)
    return items


def get_all(path, pattern):
    items = []
    for item in path.rglob(pattern):
        items.append(item)
    return items


if args.type == 'd':
    items = get_dirs(p, args.name)
if args.type == 'f':
    items = get_files(p, args.name)
if args.type == 'all':
    items = get_all(p, args.name)


def execute(item, command):
    subprocess.run([command, item])


for item in items:
    execute(item, args.exec)
