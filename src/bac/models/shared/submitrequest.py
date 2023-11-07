"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .jobcreatepayload import JobCreatePayload
from bac import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmitRequest:
    client_public_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_public_key') }})
    r"""The base64-encoded public key of the client:"""
    payload: JobCreatePayload = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload') }})
    r"""The data needed to cancel a running job on the network"""
    signature: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signature') }})
    r"""A base64-encoded signature of the data, signed by the client:"""
    

