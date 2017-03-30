import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor    # allows for the 'next()' statement.

spinner = spinning_cursor()

for item in range(50):
    sys.stdout.write('downloading ')
    sys.stdout.write(spinner.next())
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b')