#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

<<<<<<< HEAD
def print_summary():
    print(f'File size: {total_file_size}', flush=True)
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f'{key}: {status_codes[key]}', flush=True)
=======
    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']
>>>>>>> 588d099ebf0c83239817571f17cf4f980b6f5093


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
<<<<<<< HEAD
            line_count += 1
            update_metrics(line.strip())
            if line_count % 10 == 0:
                print_summary()
=======
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
>>>>>>> 588d099ebf0c83239817571f17cf4f980b6f5093
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()

# #!/usr/bin/python3
# """Log parsing module"""
# import sys
# import re

# log_format = re.compile(
#     r'^(\d{1,3}\.){3}\d{1,3} - \[(.*?)\] '
#     r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
# )

# total_file_size = 0
# line_count = 0
# status_codes = {
#     200: 0,
#     301: 0,
#     400: 0,
#     401: 0,
#     403: 0,
#     404: 0,
#     405: 0,
#     500: 0,
# }


# def update_metrics(line):
#     """
#     Update metrics with the information from the log line
#     """
#     global total_file_size, status_codes

#     match = log_format.match(line)
#     if match:
#         file_size = int(match.group(4))
#         total_file_size += file_size

#         status_code = int(match.group(3))
#         if status_code in status_codes:
#             status_codes[status_code] += 1


# def print_summary():
#     """
#     Print the metrics summary
#     """
#     print(f'File size: {total_file_size}')
#     for key in sorted(status_codes.keys()):
#         if status_codes[key] > 0:
#             print(f'{key}: {status_codes[key]}')


# if __name__ == '__main__':
#     try:
#         for line in sys.stdin:
#             line_count += 1
#             update_metrics(line.strip())
#             if line_count % 10 == 0:
#                 print_summary()
#     except (KeyboardInterrupt, EOFError):
#         print_summary()
