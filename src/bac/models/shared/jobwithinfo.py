"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import job as shared_job
from ..shared import jobhistory as shared_jobhistory
from ..shared import jobstate as shared_jobstate
from bac import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class JobWithInfo:
    history: Optional[list[shared_jobhistory.JobHistory]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('History'), 'exclude': lambda f: f is None }})
    r"""History of changes to the job state. Not always populated in the job description"""
    job: Optional[shared_job.Job] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Job'), 'exclude': lambda f: f is None }})
    r"""Job info"""
    state: Optional[shared_jobstate.JobState] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('State'), 'exclude': lambda f: f is None }})
    r"""The current state of the job"""
    
