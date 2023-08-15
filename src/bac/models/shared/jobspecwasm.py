"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import storagespec as shared_storagespec
from bac import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class JobSpecWasm:
    entry_module: Optional[shared_storagespec.StorageSpec] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('EntryModule'), 'exclude': lambda f: f is None }})
    r"""The module that contains the WASM code to start running."""
    entry_point: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('EntryPoint'), 'exclude': lambda f: f is None }})
    r"""The name of the function in the EntryModule to call to run the job. For
    WASI jobs, this will always be `_start`, but jobs can choose to call
    other WASM functions instead. The EntryPoint must be a zero-parameter
    zero-result function.
    """
    environment_variables: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('EnvironmentVariables'), 'exclude': lambda f: f is None }})
    r"""The variables available in the environment of the running program."""
    import_modules: Optional[list[shared_storagespec.StorageSpec]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ImportModules'), 'exclude': lambda f: f is None }})
    r"""TODO #880: Other WASM modules whose exports will be available as imports
    to the EntryModule.
    """
    parameters: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Parameters'), 'exclude': lambda f: f is None }})
    r"""The arguments supplied to the program (i.e. as ARGV)."""
    
