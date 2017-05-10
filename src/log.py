import sys
import logging

""" Basic logger object.
It will emit the log statements to stderr.
Default loglevel is INFO. If --debug switch is specified in commandline argument,
set loglevel to DEBUG.
"""

__all__ = ["logger"]
loglevel = logging.DEBUG if "--debug" in sys.argv else logging.INFO
logging.basicConfig(level=loglevel)
logger = logging.getLogger("contacts")
