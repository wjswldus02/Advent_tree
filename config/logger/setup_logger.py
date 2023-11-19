import logging
from logging import handlers
import sys


logger = logging.getLogger("advent-tree-log")
logger.handlers = []
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter("%(asctime)s - [%(levelname)s: %(name)s] %(message)s")

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(log_format)
logger.addHandler(ch)

fh = handlers.RotatingFileHandler("log/advent_tree.log", maxBytes=(1048576 * 5), backupCount=7, encoding="utf-8")
fh.setFormatter(log_format)
logger.addHandler(fh)
