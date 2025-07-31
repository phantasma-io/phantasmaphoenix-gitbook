# ChainApi

## swagger\_client.ChainApi

All URIs are relative to _/_

| Method                        | HTTP request              | Description |
| ----------------------------- | ------------------------- | ----------- |
| **api\_v1\_get\_chains\_get** | **GET** /api/v1/GetChains |             |

## **api\_v1\_get\_chains\_get**

> list\[ChainResult] api\_v1\_get\_chains\_get()

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChainApi()

try:
    api_response = api_instance.api_v1_get_chains_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChainApi->api_v1_get_chains_get: %s\n" % e)
```

#### Parameters

This endpoint does not need any parameter.

#### Return type

**list\[ChainResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
