"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .buildversion import BuildVersion
from .connectedpeers import ConnectedPeers
from .debug import Debug
from .healthz import Healthz
from .hostnodeid import HostNodeID
from .job import Job
from .jobevents import JobEvents
from .joblogs import JobLogs
from .jobs import Jobs
from .livez import Livez
from .logz import Logz
from .nodeinfo import NodeInfo
from .nodes import Nodes
from .readyz import Readyz
from .requesterdebug import RequesterDebug
from .results import Results
from .sdkconfiguration import SDKConfiguration
from .states import States
from .varz import Varz
from bac import utils
from typing import Dict

class Bac:
    r"""Bacalhau API: This page is the reference of the Bacalhau REST API. Project docs are available at https://docs.bacalhau.org/. Find more information about Bacalhau at https://github.com/bacalhau-project/bacalhau."""
    job: Job
    debug: Debug
    healthz: Healthz
    host_node_id: HostNodeID
    livez: Livez
    logz: Logz
    node_info: NodeInfo
    connected_peers: ConnectedPeers
    readyz: Readyz
    requester_debug: RequesterDebug
    job_events: JobEvents
    jobs: Jobs
    job_logs: JobLogs
    nodes: Nodes
    results: Results
    states: States
    varz: Varz
    build_version: BuildVersion

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, None, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.job = Job(self.sdk_configuration)
        self.debug = Debug(self.sdk_configuration)
        self.healthz = Healthz(self.sdk_configuration)
        self.host_node_id = HostNodeID(self.sdk_configuration)
        self.livez = Livez(self.sdk_configuration)
        self.logz = Logz(self.sdk_configuration)
        self.node_info = NodeInfo(self.sdk_configuration)
        self.connected_peers = ConnectedPeers(self.sdk_configuration)
        self.readyz = Readyz(self.sdk_configuration)
        self.requester_debug = RequesterDebug(self.sdk_configuration)
        self.job_events = JobEvents(self.sdk_configuration)
        self.jobs = Jobs(self.sdk_configuration)
        self.job_logs = JobLogs(self.sdk_configuration)
        self.nodes = Nodes(self.sdk_configuration)
        self.results = Results(self.sdk_configuration)
        self.states = States(self.sdk_configuration)
        self.varz = Varz(self.sdk_configuration)
        self.build_version = BuildVersion(self.sdk_configuration)
    