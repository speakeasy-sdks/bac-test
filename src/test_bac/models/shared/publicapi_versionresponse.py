"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import model_buildversioninfo as shared_model_buildversioninfo
from dataclasses_json import Undefined, dataclass_json
from test_bac import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PublicapiVersionResponse:
    r"""OK"""
    build_version_info: Optional[shared_model_buildversioninfo.ModelBuildVersionInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('build_version_info'), 'exclude': lambda f: f is None }})
    

