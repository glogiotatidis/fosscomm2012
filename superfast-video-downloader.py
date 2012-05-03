#!/usr/bin/env python
import subprocess
import sys
import time

def main():
    while True:
        proc = subprocess.Popen(['/usr/bin/wget', '-c', sys.argv[1]])
        time.sleep(5)
        proc.kill()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "%s <url>" % sys.argv[0]
        sys.exit(-1)

    main()


