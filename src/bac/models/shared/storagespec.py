"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .s3storagespec import S3StorageSpec
from .storagesourcetype import StorageSourceType
from bac import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StorageSpec:
    cid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CID'), 'exclude': lambda f: f is None }})
    r"""The unique ID of the data, where it makes sense (for example, in an
    IPFS storage spec this will be the data's CID).
    NOTE: The below is capitalized to match IPFS & IPLD (even though it's out of golang fmt)
    """
    metadata: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Metadata'), 'exclude': lambda f: f is None }})
    r"""Additional properties specific to each driver"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Name'), 'exclude': lambda f: f is None }})
    r"""Name of the spec's data, for reference."""
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Path'), 'exclude': lambda f: f is None }})
    r"""The path that the spec's data should be mounted on, where it makes
    sense (for example, in a Docker storage spec this will be a filesystem
    path).
    """
    read_write: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ReadWrite'), 'exclude': lambda f: f is None }})
    r"""Allow write access for locally mounted inputs"""
    repo: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Repo'), 'exclude': lambda f: f is None }})
    r"""URL of the git Repo to clone"""
    s3: Optional[S3StorageSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('S3'), 'exclude': lambda f: f is None }})
    source_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('SourcePath'), 'exclude': lambda f: f is None }})
    r"""The path of the host data if we are using local directory paths"""
    storage_source: Optional[StorageSourceType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('StorageSource'), 'exclude': lambda f: f is None }})
    r"""StorageSource is the abstract source of the data. E.g. a storage source
    might be a URL download, but doesn't specify how the execution engine
    does the download or what it will do with the downloaded data.
    """
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('URL'), 'exclude': lambda f: f is None }})
    r"""Source URL of the data"""
    

