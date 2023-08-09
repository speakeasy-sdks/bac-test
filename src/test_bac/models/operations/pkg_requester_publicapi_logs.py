"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional



@dataclasses.dataclass
class PkgRequesterPublicapiLogsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    pkg_requester_publicapi_logs_200_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""OK"""
    pkg_requester_publicapi_logs_400_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""Bad Request"""
    pkg_requester_publicapi_logs_401_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""Unauthorized"""
    pkg_requester_publicapi_logs_403_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""Forbidden"""
    pkg_requester_publicapi_logs_500_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

