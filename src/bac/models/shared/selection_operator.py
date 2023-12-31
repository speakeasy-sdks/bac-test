"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class SelectionOperator(str, Enum):
    DOES_NOT_EXIST = '!'
    EQUALS = '='
    DOUBLE_EQUALS = '=='
    IN = 'in'
    NOT_EQUALS = '!='
    NOT_IN = 'notin'
    EXISTS = 'exists'
    GREATER_THAN = 'gt'
    LESS_THAN = 'lt'
