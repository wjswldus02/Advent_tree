import logging
from logging import handlers
import sys


logger = logging.getLogger("advent-tree-log")
logger.handlers = []
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter("%(asctime)s - [%(levelname)s: %(name)s] %(message)s")
test_message = "Test log message"

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(log_format)
logger.addHandler(ch)

fh = handlers.RotatingFileHandler("log/advent_tree.log", maxBytes=(1048576 * 5), backupCount=7, encoding="utf-8")
fh.setFormatter(log_format)
logger.addHandler(fh)

print("Formatter Format:", log_format._fmt)

print(
    "Formatted Log Message:",
    log_format.format(logging.LogRecord("advent-tree-log", logging.DEBUG, "", 0, test_message, (), None, None)),
)
logger.info("something")
