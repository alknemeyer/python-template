__version__ = "0.0.1"

#
import logging

_logger = logging.getLogger(__name__)


def do_something():
    """Does something!"""
    _logger.warning(f"This package ({__package__}) doesn't do anything")
