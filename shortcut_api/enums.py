"""
:authors: vrohlfs
:license: n|a

:copyright: n|a
"""

from enum import IntEnum, Enum, auto

class HttpRequestTypes(IntEnum):
    """ Enum the types of HTTP requests """
    GET = auto()

    POST = auto()

    PUT = auto()

    DELETE = auto()

    BAD_TYPE = auto()

class ResponseCodes(Enum):
    """ Status codes response to the HTTP request """
    OK = (200, 201)

    SCHEMA_MISMATCH = 400

    RESOURCE_DOES_NOT_EXIST = 404

    UNPROCESSIBLE = 422

    NO_CONTENT = 204

    TOO_MATCH_REQUEST = 429 




    