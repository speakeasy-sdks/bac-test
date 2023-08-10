"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import jobhistorytype as shared_jobhistorytype
from ..shared import statechange_model_executionstatetype as shared_statechange_model_executionstatetype
from ..shared import statechange_model_jobstatetype as shared_statechange_model_jobstatetype
from dataclasses_json import Undefined, dataclass_json
from test_bac import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class JobHistory:
    comment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Comment'), 'exclude': lambda f: f is None }})
    compute_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ComputeReference'), 'exclude': lambda f: f is None }})
    execution_state: Optional[shared_statechange_model_executionstatetype.StateChangeModelExecutionStateType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ExecutionState'), 'exclude': lambda f: f is None }})
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('JobID'), 'exclude': lambda f: f is None }})
    job_state: Optional[shared_statechange_model_jobstatetype.StateChangeModelJobStateType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('JobState'), 'exclude': lambda f: f is None }})
    new_version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NewVersion'), 'exclude': lambda f: f is None }})
    node_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NodeID'), 'exclude': lambda f: f is None }})
    time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Time'), 'exclude': lambda f: f is None }})
    type: Optional[shared_jobhistorytype.JobHistoryType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Type'), 'exclude': lambda f: f is None }})
    
