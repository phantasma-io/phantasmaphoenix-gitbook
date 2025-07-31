# RpcApi

## swagger\_client.RpcApi

All URIs are relative to _/_

| Method        | HTTP request  | Description |
| ------------- | ------------- | ----------- |
| **rpc\_post** | **POST** /rpc |             |

## **rpc\_post**

> RpcResponse rpc\_post(body=body)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RpcApi()
body = swagger_client.RpcRequest() # RpcRequest |  (optional)

try:
    api_response = api_instance.rpc_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RpcApi->rpc_post: %s\n" % e)
```

#### Parameters

| Name     | Type           | Description | Notes       |
| -------- | -------------- | ----------- | ----------- |
| **body** | **RpcRequest** |             | \[optional] |

#### Return type

**RpcResponse**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: application/json, text/json, application/\*+json
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
