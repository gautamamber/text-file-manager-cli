import argparse

# create a parser
parser = argparse.ArgumentParser(description="An additional program")

# add argument
parser.add_argument("add", nargs='*', metavar="num", type=int, help="all number seperated by space will be added")

"""
In above line of code
add : it means a command to perform operation
nargs : Number of arguments, * means any number of arguments (0 to n)
metavar: A name for the argument
type: instance of argument (int, str etc)
help: help message
"""

args = parser.parse_args()

"""
Print sum of integer numbers
"""
if len(args.add) != 0:
    print(args.add)
    print(sum(args.add))
