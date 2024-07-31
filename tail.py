import json
import re
import time
from datetime import datetime

bannedlist = 'valheim-server/config/bannedlist.txt'


def follow(file):
    file.seek(0, 2)  # Go to the end of the file

    while True:
        line = file.readline()

        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue

        yield line


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


def parse(lines):
    for line in lines:
        dt, _, sjson = re.split('\t', line.strip())
        yield (datetime.fromisoformat(dt), json.loads(sjson))


if __name__ == '__main__':
    logfile = open('logs/buffer/buffer.b61debe1b38324213fd6eed25250283f0.log')
    loglines = follow(logfile)
    loglines = grep('debugmode', loglines)
    loglines = parse(loglines)

    for dt, j in loglines:
        print(j['log'])
