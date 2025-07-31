# SaleApi

## swagger\_client.SaleApi

All URIs are relative to _/_

| Method                                    | HTTP request                      | Description |
| ----------------------------------------- | --------------------------------- | ----------- |
| **api\_v1\_get\_latest\_sale\_hash\_get** | **GET** /api/v1/GetLatestSaleHash |             |
| **api\_v1\_get\_sale\_get**               | **GET** /api/v1/GetSale           |             |

## **api\_v1\_get\_latest\_sale\_hash\_get**

> str api\_v1\_get\_latest\_sale\_hash\_get()

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SaleApi()

try:
    api_response = api_instance.api_v1_get_latest_sale_hash_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->api_v1_get_latest_sale_hash_get: %s\n" % e)
```

#### Parameters

This endpoint does not need any parameter.

#### Return type

**str**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_sale\_get**

> CrowdsaleResult api\_v1\_get\_sale\_get(hash\_text=hash\_text)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SaleApi()
hash_text = 'hash_text_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_sale_get(hash_text=hash_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaleApi->api_v1_get_sale_get: %s\n" % e)
```

#### Parameters

| Name           | Type    | Description | Notes       |
| -------------- | ------- | ----------- | ----------- |
| **hash\_text** | **str** |             | \[optional] |

#### Return type

**CrowdsaleResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
