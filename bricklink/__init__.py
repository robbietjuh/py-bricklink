'''

    bricklink
    ---------

    Python implementation of the Bricklink API. Basic usage:

        >>> import bricklink
        >>> client = bricklink.ApiClient(consumer_key='foo',
        >>>                              consumer_secret='bar',
        >>>                              access_token='foo',
        >>>                              access_token_secret='bar')

'''

__all__ = ['ApiClient']

from .api import ApiClient
from .exceptions import *
from .__about__ import (__title__, __version_info__, __version__, __author__,
                        __license__, __copyright__)

(__title__, __version_info__, __version__, __author__, __license__,
__copyright__)