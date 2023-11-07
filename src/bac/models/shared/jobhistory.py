"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .jobhistorytype import JobHistoryType
from .statechange_model_executionstatetype import StateChangeModelExecutionStateType
from .statechange_model_jobstatetype import StateChangeModelJobStateType
from bac import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JobHistory:
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Comment'), 'exclude': lambda f: f is None }})
    compute_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ComputeReference'), 'exclude': lambda f: f is None }})
    execution_state: Optional[StateChangeModelExecutionStateType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ExecutionState'), 'exclude': lambda f: f is None }})
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('JobID'), 'exclude': lambda f: f is None }})
    job_state: Optional[StateChangeModelJobStateType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('JobState'), 'exclude': lambda f: f is None }})
    new_version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NewVersion'), 'exclude': lambda f: f is None }})
    node_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NodeID'), 'exclude': lambda f: f is None }})
    time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Time'), 'exclude': lambda f: f is None }})
    type: Optional[JobHistoryType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Type'), 'exclude': lambda f: f is None }})
    

