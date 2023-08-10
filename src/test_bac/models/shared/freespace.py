"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import mountstatus as shared_mountstatus
from dataclasses_json import Undefined, dataclass_json
from test_bac import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FreeSpace:
    ipfs_mount: Optional[shared_mountstatus.MountStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('IPFSMount'), 'exclude': lambda f: f is None }})
    root: Optional[shared_mountstatus.MountStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('root'), 'exclude': lambda f: f is None }})
    tmp: Optional[shared_mountstatus.MountStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tmp'), 'exclude': lambda f: f is None }})
    
