#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
import sys
import re

status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0


def print_stats(status_dict, total_size):
    """
    Method to print stats:
    total file size: File size: <total size>
    where <total size> is the sum of all previous
    <file size>
    """

    print("File size: {}".format(total_size))
    for key, val in sorted(status_dict.items()):
        if val != 0:
            print("{}: {}".format(key, val))


def check_log_line_format(log_line):
    """
    check if the log line follow the expected format
    """
    pattern = (
        r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    )
    match = re.match(pattern, log_line)

    return bool(match)


try:
    for line in sys.stdin:
        if check_log_line_format(line):
            line_parsed = line.split(" ")
            num = line_parsed[-2]
            size = int(line_parsed[-1])
            if num in status.keys():
                status[num] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print_stats(status, total_size)

except Exception:
    pass

finally:
    print_stats(status, total_size)
