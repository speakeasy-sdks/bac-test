"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import model_nodeinfo as shared_model_nodeinfo
from typing import Optional



@dataclasses.dataclass
class PkgRequesterPublicapiNodesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_node_infos: Optional[list[shared_model_nodeinfo.ModelNodeInfo]] = dataclasses.field(default=None)
    r"""OK"""
    pkg_requester_publicapi_nodes_500_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""Internal Server Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

