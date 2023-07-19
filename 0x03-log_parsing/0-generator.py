#!/usr/bin/python3
'''A script that generates random HTTP request logs.
'''
import sys
import signal

status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
total_size = 0
lines_by_status = {code: 0 for code in status_codes}

def print_statistics(signum=None, frame=None):
    print("Total file size:", total_size)
    for code in sorted(lines_by_status.keys()):
        if lines_by_status[code] > 0:
            print(f"{code}: {lines_by_status[code]}")
    sys.exit(0)

signal.signal(signal.SIGINT, print_statistics)

try:
    for line_number, line in enumerate(sys.stdin, start=1):
        try:
            _, _, _, _, _, status_code, file_size_str = line.split()[3:10]
            status_code = int(status_code)
            file_size = int(file_size_str)
            if status_code in status_codes:
                lines_by_status[status_code] += 1
                total_size += file_size

            if line_number % 10 == 0:
                print_statistics()
        except ValueError:
            # Skip the line if it doesn't match the expected format
            continue
except KeyboardInterrupt:
    print_statistics()
