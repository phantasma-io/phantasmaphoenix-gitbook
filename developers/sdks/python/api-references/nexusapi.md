# NexusApi

## swagger\_client.NexusApi

All URIs are relative to _/_

| Method                       | HTTP request             | Description |
| ---------------------------- | ------------------------ | ----------- |
| **api\_v1\_get\_nexus\_get** | **GET** /api/v1/GetNexus |             |

## **api\_v1\_get\_nexus\_get**

> NexusResult api\_v1\_get\_nexus\_get(extended=extended)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NexusApi()
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_nexus_get(extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NexusApi->api_v1_get_nexus_get: %s\n" % e)
```

#### Parameters

| Name         | Type     | Description | Notes                           |
| ------------ | -------- | ----------- | ------------------------------- |
| **extended** | **bool** |             | \[optional] \[default to false] |

#### Return type

**NexusResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
