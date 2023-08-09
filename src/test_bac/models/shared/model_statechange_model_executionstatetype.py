"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import model_executionstatetype as shared_model_executionstatetype
from dataclasses_json import Undefined, dataclass_json
from test_bac import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ModelStateChangeModelExecutionStateType:
    new: Optional[shared_model_executionstatetype.ModelExecutionStateType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('New'), 'exclude': lambda f: f is None }})
    previous: Optional[shared_model_executionstatetype.ModelExecutionStateType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Previous'), 'exclude': lambda f: f is None }})
    

