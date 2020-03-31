# help (-h --help)
# 3 flags
# 3 options (with an argument)
# n additional positional arguments
# they support wildcards

# flags:    -u (uppercase)
#           -l (lowercase)
#           -s (print a smiley face at the end)

import argparse

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument(
    "-l", "--lowercase", action="store_true", help="print a lowercase message"
)
parser.add_argument(
    "-u", "--uppercase", action="store_true", help="print an uppercase message"
)
parser.add_argument("-s", "--smiley", action="store_true", help="print a smiley :)")

parser.add_argument("-n", "--name", help="print your personal message")
parser.add_argument("-a", "--age", help="print your age")

args = parser.parse_args()

message = "Hello there!"

if args.smiley:
    message += " :)"

if args.name:
    message = message.replace("there", args.name)

if args.age:
    message = f"{message}, you are {args.age} years old"

if args.uppercase:
    message = message.upper()

if args.lowercase:
    message = message.lower()


print(message)

