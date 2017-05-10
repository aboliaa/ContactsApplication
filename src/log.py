import sys
import logging

__all__ = ["logger"]
loglevel = logging.DEBUG if "--debug" in sys.argv else logging.INFO
logging.basicConfig(level=loglevel)
logger = logging.getLogger("contacts")
