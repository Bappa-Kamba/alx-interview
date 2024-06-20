#!/usr/bin/python3
"""Log parsing module"""
import sys
import signal
import re

log_format = re.compile(
    r'^(\d{1,3}\.){3}\d{1,3} - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

total_file_size = 0
line_count = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}


def handle_sigInt(sigInt, frame):
    print_summary()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigInt)


def update_metrics(line):
    global total_file_size, status_codes

    match = log_format.match(line)
    if match:
        file_size = int(match.group(4))
        total_file_size += file_size

        status_code = int(match.group(3))
        if status_code in status_codes:
            status_codes[status_code] += 1


def print_summary():
    print(f'File size: {total_file_size}')
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f'{key}: {status_codes[key]}')


try:
    for line in sys.stdin:
        line_count += 1
        update_metrics(line.strip())
        if line_count % 10 == 0:
            print_summary()
except (KeyboardInterrupt, EOFError):
    print_summary()
