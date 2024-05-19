import argparse
from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta

@dataclass
class Configs:
    end: str
    start: str

    duration: str
    time: str

    format: str

def build_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser(description='tgap: Perform time-related calculations')
    subparsers = parser.add_subparsers(dest='command')

    # diff subcommand
    diff_parser = subparsers.add_parser('diff', help='Calculate the difference between two times')
    diff_parser.add_argument('end', type=str, help='The end time')
    diff_parser.add_argument('-s', '--start', type=str, default=None, help='The start time (default is current time)')
    diff_parser.add_argument('-f', '--format', type=str, default='%Y-%m-%d %H:%M:%S', help='The time format (default is %%Y-%%m-%%d %%H:%%M:%%S)')
    diff_parser.set_defaults(func=calculate_diff)

    # add subcommand
    add_parser = subparsers.add_parser('add', help='Add a duration to a specified time')
    add_parser.add_argument('duration', type=str, help='The duration to add')
    add_parser.add_argument('-t', '--time', type=str, default=None, help='The initial time (default is current time)')
    add_parser.add_argument('-f', '--format', type=str, default='%Y-%m-%d %H:%M:%S', help='The time format (default is %%Y-%%m-%%d %%H:%%M:%%S)')
    add_parser.set_defaults(func=add_duration)

    # sub subcommand
    sub_parser = subparsers.add_parser('sub', help='Subtract a duration from a specified time')
    sub_parser.add_argument('duration', type=str, help='The duration to subtract')
    sub_parser.add_argument('-t', '--time', type=str, default=None, help='The initial time (default is current time)')
    sub_parser.add_argument('-f', '--format', type=str, default='%Y-%m-%d %H:%M:%S', help='The time format (default is %%Y-%%m-%%d %%H:%%M:%%S)')
    sub_parser.set_defaults(func=subtract_duration)

    return parser

def calculate_diff(configs: Configs) -> str:
    end = parse_time(configs.end, configs.format)
    if configs.start:
        start = parse_time(configs.start, configs.format)
    else:
        start = datetime.now()
    result = abs(end - start)
    return result

def add_duration(configs: Configs) -> str:
    base_time, delta = convert_configs(configs)
    result = base_time + delta
    return result

def subtract_duration(configs: Configs) -> str:
    base_time, delta = convert_configs(configs)
    result = base_time - delta
    return result

def convert_configs(configs: Configs) -> (datetime, timedelta):
    delta = parse_duration(configs.duration)
    if configs.time:
        base_time = parse_time(configs.time, configs.format)
    else:
        base_time = datetime.now()
    return base_time, delta

def parse_duration(duration: str) -> timedelta:
    """Parses a duration string like "1d 3h 30m" into a timedelta object"""
    result = timedelta()
    units = {"d": "days", "h": "hours", "m": "minutes", "s": "seconds"}
    for part in duration.split():
        unit = part[-1]
        if unit in units:
            value = int(part[:-1])
            result += timedelta(**{units[unit]: value})
    return result

def parse_time(time: str, time_format: str) -> datetime:
    result = datetime.strptime(time, time_format)
    return result


