import argparse
from argparse import ArgumentParser

def build_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser(description='tgap: Perform time-related calculations')
    subparsers = parser.add_subparsers(dest='command')

    # diff subcommand
    diff_parser = subparsers.add_parser('diff', help='Calculate the difference between two times')
    diff_parser.add_argument('end', type=str, help='The end time')
    diff_parser.add_argument('-s', '--start', type=str, default=None, help='The start time (default is current time)')
    diff_parser.add_argument('-f', '--format', type=str, default='%Y-%m-%d %H:%M:%S', help='The time format (default is %%Y-%%m-%%d %%H:%%M:%%S)')

    # add subcommand
    add_parser = subparsers.add_parser('add', help='Add a duration to a specified time')
    add_parser.add_argument('duration', type=str, help='The duration to add')
    add_parser.add_argument('-t', '--time', type=str, default=None, help='The initial time (default is current time)')
    add_parser.add_argument('-f', '--format', type=str, default='%Y-%m-%d %H:%M:%S', help='The time format (default is %%Y-%%m-%%d %%H:%%M:%%S)')

    # sub subcommand
    sub_parser = subparsers.add_parser('sub', help='Subtract a duration from a specified time')
    sub_parser.add_argument('duration', type=str, help='The duration to subtract')
    sub_parser.add_argument('-t', '--time', type=str, default=None, help='The initial time (default is current time)')
    sub_parser.add_argument('-f', '--format', type=str, default='%Y-%m-%d %H:%M:%S', help='The time format (default is %%Y-%%m-%%d %%H:%%M:%%S)')

    return parser
