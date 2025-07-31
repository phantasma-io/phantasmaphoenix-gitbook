# ConnectionApi

## swagger\_client.ConnectionApi

All URIs are relative to _/_

| Method                                      | HTTP request                          | Description |
| ------------------------------------------- | ------------------------------------- | ----------- |
| **api\_v1\_abci\_query\_get**               | **GET** /api/v1/abci\_query           |             |
| **api\_v1\_get\_validators\_settings\_get** | **GET** /api/v1/GetValidatorsSettings |             |
| **api\_v1\_health\_get**                    | **GET** /api/v1/health                |             |
| **api\_v1\_net\_info\_get**                 | **GET** /api/v1/net\_info             |             |
| **api\_v1\_request\_block\_get**            | **GET** /api/v1/request\_block        |             |
| **api\_v1\_status\_get**                    | **GET** /api/v1/status                |             |

## **api\_v1\_abci\_query\_get**

> ResultAbciQuery api\_v1\_abci\_query\_get(path=path, data=data, height=height, prove=prove)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
path = 'path_example' # str |  (optional)
data = 'data_example' # str |  (optional)
height = 0 # int |  (optional) (default to 0)
prove = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_abci_query_get(path=path, data=data, height=height, prove=prove)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_abci_query_get: %s\n" % e)
```

#### Parameters

| Name       | Type     | Description | Notes                           |
| ---------- | -------- | ----------- | ------------------------------- |
| **path**   | **str**  |             | \[optional]                     |
| **data**   | **str**  |             | \[optional]                     |
| **height** | **int**  |             | \[optional] \[default to 0]     |
| **prove**  | **bool** |             | \[optional] \[default to false] |

#### Return type

**ResultAbciQuery**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_validators\_settings\_get**

> list\[ValidatorSettings] api\_v1\_get\_validators\_settings\_get()

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_get_validators_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_get_validators_settings_get: %s\n" % e)
```

#### Parameters

This endpoint does not need any parameter.

#### Return type

**list\[ValidatorSettings]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_health\_get**

> ResultHealth api\_v1\_health\_get()

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_health_get: %s\n" % e)
```

#### Parameters

This endpoint does not need any parameter.

#### Return type

**ResultHealth**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_net\_info\_get**

> ResultNetInfo api\_v1\_net\_info\_get()

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_net_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_net_info_get: %s\n" % e)
```

#### Parameters

This endpoint does not need any parameter.

#### Return type

**ResultNetInfo**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_request\_block\_get**

> ResultAbciQuery api\_v1\_request\_block\_get(height=height)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
height = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.api_v1_request_block_get(height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_request_block_get: %s\n" % e)
```

#### Parameters

| Name       | Type    | Description | Notes                       |
| ---------- | ------- | ----------- | --------------------------- |
| **height** | **int** |             | \[optional] \[default to 0] |

#### Return type

**ResultAbciQuery**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_status\_get**

> ResultStatus api\_v1\_status\_get()

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    api_response = api_instance.api_v1_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->api_v1_status_get: %s\n" % e)
```

#### Parameters

This endpoint does not need any parameter.

#### Return type

**ResultStatus**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
