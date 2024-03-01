"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from bac import utils
from bac._hooks import HookContext
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
        hook_ctx = HookContext(operation_id='getStates', oauth2_scopes=[], security_source=None)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/requester/states'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, shared.StateRequest, "request", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.client
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','4XX','500','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
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

    