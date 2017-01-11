import sys
import signal, time, logbook
from .core import hmm

log = logbook.Logger('APP')
handler = logbook.FileHandler('app.log')

def log_info(msg):
    with handler.applicationbound():
        log.info(msg)

def log_warn(msg):
    with handler.applicationbound():
        log.warn(msg)

def sigterm_handler(signum, frame):
    log_warn('Someone killed me.')
    exit(0)

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

    signal.signal(signal.SIGTERM, sigterm_handler)
    while True:
        log_info('I am alive.')
        hmm()
        time.sleep(1)

if __name__ == "__main__":
    main()