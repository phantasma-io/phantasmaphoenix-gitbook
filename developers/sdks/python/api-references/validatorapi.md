# ValidatorApi

## swagger\_client.ValidatorApi

All URIs are relative to _/_

| Method                                  | HTTP request                         | Description |
| --------------------------------------- | ------------------------------------ | ----------- |
| **api\_v1\_get\_validators\_get**       | **GET** /api/v1/GetValidators        |             |
| **api\_v1\_get\_validators\_type\_get** | **GET** /api/v1/GetValidators/{type} |             |

## **api\_v1\_get\_validators\_get**

> list\[ValidatorResult] api\_v1\_get\_validators\_get()

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidatorApi()

try:
    api_response = api_instance.api_v1_get_validators_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidatorApi->api_v1_get_validators_get: %s\n" % e)
```

#### Parameters

This endpoint does not need any parameter.

#### Return type

**list\[ValidatorResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_validators\_type\_get**

> list\[ValidatorResult] api\_v1\_get\_validators\_type\_get(type)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ValidatorApi()
type = 'type_example' # str | 

try:
    api_response = api_instance.api_v1_get_validators_type_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidatorApi->api_v1_get_validators_type_get: %s\n" % e)
```

#### Parameters

| Name     | Type    | Description | Notes |
| -------- | ------- | ----------- | ----- |
| **type** | **str** |             |       |

#### Return type

**list\[ValidatorResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
