"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import badrequest as shared_badrequest
from ..shared import cancelresponse as shared_cancelresponse
from ..shared import forbidden as shared_forbidden
from ..shared import internalservererror as shared_internalservererror
from ..shared import unauthorized as shared_unauthorized
from typing import Optional



@dataclasses.dataclass
class CancelJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bad_request: Optional[shared_badrequest.BadRequest] = dataclasses.field(default=None)
    r"""Bad Request"""
    cancel_response: Optional[shared_cancelresponse.CancelResponse] = dataclasses.field(default=None)
    r"""OK"""
    forbidden: Optional[shared_forbidden.Forbidden] = dataclasses.field(default=None)
    r"""Forbidden"""
    internal_server_error: Optional[shared_internalservererror.InternalServerError] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    unauthorized: Optional[shared_unauthorized.Unauthorized] = dataclasses.field(default=None)
    r"""Unauthorized"""
    

