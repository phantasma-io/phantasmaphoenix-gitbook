# OrganizationApi

## swagger\_client.OrganizationApi

All URIs are relative to _/_

| Method                                        | HTTP request                          | Description |
| --------------------------------------------- | ------------------------------------- | ----------- |
| **api\_v1\_get\_organization\_by\_name\_get** | **GET** /api/v1/GetOrganizationByName |             |
| **api\_v1\_get\_organization\_get**           | **GET** /api/v1/GetOrganization       |             |
| **api\_v1\_get\_organizations\_get**          | **GET** /api/v1/GetOrganizations      |             |

## **api\_v1\_get\_organization\_by\_name\_get**

> OrganizationResult api\_v1\_get\_organization\_by\_name\_get(name=name)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_organization_by_name_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v1_get_organization_by_name_get: %s\n" % e)
```

#### Parameters

| Name     | Type    | Description | Notes       |
| -------- | ------- | ----------- | ----------- |
| **name** | **str** |             | \[optional] |

#### Return type

**OrganizationResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_organization\_get**

> OrganizationResult api\_v1\_get\_organization\_get(id=id)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
id = 'id_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_organization_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v1_get_organization_get: %s\n" % e)
```

#### Parameters

| Name   | Type    | Description | Notes       |
| ------ | ------- | ----------- | ----------- |
| **id** | **str** |             | \[optional] |

#### Return type

**OrganizationResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_organizations\_get**

> list\[OrganizationResult] api\_v1\_get\_organizations\_get(extended=extended)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationApi()
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_organizations_get(extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationApi->api_v1_get_organizations_get: %s\n" % e)
```

#### Parameters

| Name         | Type     | Description | Notes                           |
| ------------ | -------- | ----------- | ------------------------------- |
| **extended** | **bool** |             | \[optional] \[default to false] |

#### Return type

**list\[OrganizationResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
