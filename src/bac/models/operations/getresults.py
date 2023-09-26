"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import badrequest as shared_badrequest
from ..shared import internalservererror as shared_internalservererror
from ..shared import resultsresponse as shared_resultsresponse
from typing import Optional



@dataclasses.dataclass
class GetResultsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bad_request: Optional[shared_badrequest.BadRequest] = dataclasses.field(default=None)
    r"""Bad Request"""
    internal_server_error: Optional[shared_internalservererror.InternalServerError] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    results_response: Optional[shared_resultsresponse.ResultsResponse] = dataclasses.field(default=None)
    r"""OK"""
    

