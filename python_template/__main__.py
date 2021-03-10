"""
The log level can be set via the `LOG_LEVEL` environment
variable. For example:

    $ export LOG_LEVEL="DEBUG" && python -m python_template

"""

import logging
import os

import python_template

# Set up logging -- see the description of this file for usage
_log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(module)s:%(lineno)i | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level=_log_level,
)

# A simple test
python_template.do_something()
