"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .executiondesiredstate import ExecutionDesiredState
from .executionstatetype import ExecutionStateType
from .runcommandresult import RunCommandResult
from .storagespec import StorageSpec
from bac import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExecutionState:
    compute_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ComputeReference'), 'exclude': lambda f: f is None }})
    r"""Compute node reference for this job execution"""
    create_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CreateTime'), 'exclude': lambda f: f is None }})
    r"""CreateTime is the time when the job was created."""
    desired_state: Optional[ExecutionDesiredState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DesiredState'), 'exclude': lambda f: f is None }})
    r"""DesiredState is the desired state of the execution"""
    job_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('JobID'), 'exclude': lambda f: f is None }})
    r"""JobID the job id"""
    node_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('NodeId'), 'exclude': lambda f: f is None }})
    r"""which node is running this execution"""
    published_results: Optional[StorageSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('PublishedResults'), 'exclude': lambda f: f is None }})
    r"""the published results for this execution"""
    run_output: Optional[RunCommandResult] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RunOutput'), 'exclude': lambda f: f is None }})
    r"""RunOutput of the job"""
    state: Optional[ExecutionStateType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('State'), 'exclude': lambda f: f is None }})
    r"""State is the current state of the execution"""
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Status'), 'exclude': lambda f: f is None }})
    r"""an arbitrary status message"""
    update_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('UpdateTime'), 'exclude': lambda f: f is None }})
    r"""UpdateTime is the time when the job state was last updated."""
    version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Version'), 'exclude': lambda f: f is None }})
    r"""Version is the version of the job state. It is incremented every time the job state is updated."""
    

