"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .freespace import FreeSpace
from bac import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HealthInfo:
    free_space: Optional[FreeSpace] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('FreeSpace'), 'exclude': lambda f: f is None }})
    

