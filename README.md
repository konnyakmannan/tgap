# tgap

`tgap` is a command-line tool for performing various time-related calculations, such as calculating the difference between times and adding or subtracting time values.

## Features

- Calculate the difference between two times
- Add or subtract a specified duration from a given time
- Simplify commands by assuming the current time when start time or initial time is omitted
- Supports multiple time formats

## Installation

To install `tgap`, simply run:

```sh
pip install tgap
```

## Usage

### General Syntax

```sh
tgap [subcommand] [options]
```

`tgap` uses subcommands to perform different time-related calculations. The general syntax for using `tgap` is shown above.

### Subcommands

#### `diff`

Calculate the difference between two times.

```sh
tgap diff [options]
```

**Options:**

- `end`: The end time (required)
- `--start` or `-s`: The start time (optional, default is the current time in your locale)
- `--format` or `-f`: The time format (optional, default is `%Y-%m-%d %H:%M:%S`)

**Example:**

```sh
tgap diff "2024-05-14 15:30:00" -s "2024-05-14 12:00:00"
```

This command calculates the difference between "2024-05-14 15:30:00" and "2024-05-14 12:00:00".

#### `add`

Add a duration to a specified time.

```sh
tgap add [options]
```

**Options:**

- `duration`: The duration to add (required)
- `--time` or `-t`: The initial time (optional, default is the current time in your locale)
- `--format` or `-f`: The time format (optional, default is `%Y-%m-%d %H:%M:%S`)

**Example:**

```sh
tgap add "1d 3h 30m" -t "2024-05-14 12:00:00"
```

This command adds 1 day, 3 hours, and 30 minutes to "2024-05-14 12:00:00".

#### `sub`

Subtract a duration from a specified time.

```sh
tgap sub [options]
```

**Options:**

- `duration`: The duration to subtract (required)
- `--time` or `-t`: The initial time (optional, default is the current time in your locale)
- `--format` or `-f`: The time format (optional, default is `%Y-%m-%d %H:%M:%S`)

**Example:**

```sh
tgap sub "1h 45m" -t "2024-05-14 12:00:00"
```

This command subtracts 1 hour and 45 minutes from "2024-05-14 12:00:00".

## Time Formats

`tgap` supports a variety of time formats. The default format is `%Y-%m-%d %H:%M:%S`. You can specify a different format using the `--format` option. Here are a few examples of supported formats:

- `%d/%m/%Y %H:%M`
- `%m-%d-%Y %I:%M %p`
- `%Y%m%dT%H%M%S`

For a comprehensive list of supported formats, refer to the Python `datetime` module documentation.

