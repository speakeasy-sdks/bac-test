"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from bac import utils
from bac.models import errors, operations, shared
from typing import Optional

class States:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def get(self, request: shared.StateRequest) -> operations.GetStatesResponse:
        r"""Returns the state of the job-id specified in the body payload.
        Example response:

        ```json
        {
          \"state\": {
            \"Nodes\": {
              \"QmSyJ8VUd4YSPwZFJSJsHmmmmg7sd4BAc2yHY73nisJo86\": {
                \"Shards\": {
                  \"0\": {
                    \"NodeId\": \"QmSyJ8VUd4YSPwZFJSJsHmmmmg7sd4BAc2yHY73nisJo86\",
                    \"State\": \"Cancelled\",
                    \"VerificationResult\": {},
                    \"PublishedResults\": {}
                  }
                }
              },
              \"QmYgxZiySj3MRkwLSL4X2MF5F9f2PMhAE3LV49XkfNL1o3\": {
                \"Shards\": {
                  \"0\": {
                    \"NodeId\": \"QmYgxZiySj3MRkwLSL4X2MF5F9f2PMhAE3LV49XkfNL1o3\",
                    \"State\": \"Cancelled\",
                    \"VerificationResult\": {},
                    \"PublishedResults\": {}
                  }
                }
              },
              \"QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL\": {
                \"Shards\": {
                  \"0\": {
                    \"NodeId\": \"QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL\",
                    \"State\": \"Completed\",
                    \"Status\": \"Got results proposal of length: 0\",
                    \"VerificationResult\": {
                      \"Complete\": true,
                      \"Result\": true
                    },
                    \"PublishedResults\": {
                      \"StorageSource\": \"IPFS\",
                      \"Name\": \"job-9304c616-291f-41ad-b862-54e133c0149e-shard-0-host-QmdZQ7ZbhnvWY1J12XYKGHApJ6aufKyLNSvf8jZBrBaAVL\",
                      \"CID\": \"QmTVmC7JBD2ES2qGPqBNVWnX1KeEPNrPGb7rJ8cpFgtefe\"
                    },
                    \"RunOutput\": {
                      \"stdout\": \"Thu Nov 17 13:32:55 UTC 2022\n\",
                      \"stdouttruncated\": false,
                      \"stderr\": \"\",
                      \"stderrtruncated\": false,
                      \"exitCode\": 0,
                      \"runnerError\": \"\"
                    }
                  }
                }
              }
            }
          }
        }
        ```
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/requester/states'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, shared.StateRequest, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetStatesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.StateResponse])
                res.state_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.BadRequest)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 500:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.InternalServerError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    