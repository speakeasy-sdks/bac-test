"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class Publisher(int, Enum):
    PUBLISHER_UNKNOWN = 0
    PUBLISHER_NOOP = 1
    PUBLISHER_IPFS = 2
    PUBLISHER_ESTUARY = 3
    PUBLISHER_S3 = 4
    PUBLISHER_DONE = 5