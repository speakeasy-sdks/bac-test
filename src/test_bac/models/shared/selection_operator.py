"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class SelectionOperator(str, Enum):
    NOT_ = '!'
    EQUAL_ = '='
    EQUAL_EQUAL_ = '=='
    IN = 'in'
    NOT_EQUAL_ = '!='
    NOTIN = 'notin'
    EXISTS = 'exists'
    GT = 'gt'
    LT = 'lt'
