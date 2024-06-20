#!/usr/bin/python3
"""Log parsing module"""
import sys
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


def extract_input(line):
    """Extracts and parses parts of the log line."""
    match = log_format.match(line)
    if match:
        return {
            'status_code': int(match.group(3)),
            'file_size': int(match.group(4))
        }
    return None


def update_metrics(info):
    """Updates metrics with the information from the log line."""
    global total_file_size, status_codes
    if info:
        total_file_size += info['file_size']
        status_code = info['status_code']
        if status_code in status_codes:
            status_codes[status_code] += 1


def print_summary():
    """Prints the metrics summary."""
    print(f'File size: {total_file_size}', flush=True)
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f'{key}: {status_codes[key]}', flush=True)


def main():
    """Main function to read input and update metrics."""
    global line_count
    try:
        for line in sys.stdin:
            line_count += 1
            info = extract_input(line.strip())
            update_metrics(info)
            if line_count % 10 == 0:
                print_summary()
    except (KeyboardInterrupt, EOFError):
        print_summary()


if __name__ == '__main__':
    main()
test