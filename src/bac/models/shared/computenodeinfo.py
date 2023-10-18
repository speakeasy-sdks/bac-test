"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import engine as shared_engine
from ..shared import publisher as shared_publisher
from ..shared import resourceusagedata as shared_resourceusagedata
from ..shared import storagesourcetype as shared_storagesourcetype
from bac import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ComputeNodeInfo:
    available_capacity: Optional[shared_resourceusagedata.ResourceUsageData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AvailableCapacity'), 'exclude': lambda f: f is None }})
    enqueued_executions: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('EnqueuedExecutions'), 'exclude': lambda f: f is None }})
    execution_engines: Optional[List[shared_engine.Engine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ExecutionEngines'), 'exclude': lambda f: f is None }})
    max_capacity: Optional[shared_resourceusagedata.ResourceUsageData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('MaxCapacity'), 'exclude': lambda f: f is None }})
    max_job_requirements: Optional[shared_resourceusagedata.ResourceUsageData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('MaxJobRequirements'), 'exclude': lambda f: f is None }})
    publishers: Optional[List[shared_publisher.Publisher]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Publishers'), 'exclude': lambda f: f is None }})
    running_executions: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RunningExecutions'), 'exclude': lambda f: f is None }})
    storage_sources: Optional[List[shared_storagesourcetype.StorageSourceType]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StorageSources'), 'exclude': lambda f: f is None }})
    

