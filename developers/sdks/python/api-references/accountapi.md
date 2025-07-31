# AccountApi

## swagger\_client.AccountApi

All URIs are relative to _/_

| Method                                       | HTTP request                         | Description |
| -------------------------------------------- | ------------------------------------ | ----------- |
| **api\_v1\_get\_account\_get**               | **GET** /api/v1/GetAccount           |             |
| **api\_v1\_get\_accounts\_get**              | **GET** /api/v1/GetAccounts          |             |
| **api\_v1\_get\_addresses\_by\_symbol\_get** | **GET** /api/v1/GetAddressesBySymbol |             |
| **api\_v1\_look\_up\_name\_get**             | **GET** /api/v1/LookUpName           |             |

## **api\_v1\_get\_account\_get**

> AccountResult api\_v1\_get\_account\_get(account=account)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
account = 'account_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_account_get(account=account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_get_account_get: %s\n" % e)
```

#### Parameters

| Name        | Type    | Description | Notes       |
| ----------- | ------- | ----------- | ----------- |
| **account** | **str** |             | \[optional] |

#### Return type

**AccountResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_accounts\_get**

> list\[AccountResult] api\_v1\_get\_accounts\_get(account\_text=account\_text)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
account_text = 'account_text_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_accounts_get(account_text=account_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_get_accounts_get: %s\n" % e)
```

#### Parameters

| Name              | Type    | Description | Notes       |
| ----------------- | ------- | ----------- | ----------- |
| **account\_text** | **str** |             | \[optional] |

#### Return type

**list\[AccountResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_addresses\_by\_symbol\_get**

> list\[AccountResult] api\_v1\_get\_addresses\_by\_symbol\_get(symbol=symbol, extended=extended)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
symbol = 'symbol_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_addresses_by_symbol_get(symbol=symbol, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_get_addresses_by_symbol_get: %s\n" % e)
```

#### Parameters

| Name         | Type     | Description | Notes                           |
| ------------ | -------- | ----------- | ------------------------------- |
| **symbol**   | **str**  |             | \[optional]                     |
| **extended** | **bool** |             | \[optional] \[default to false] |

#### Return type

**list\[AccountResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_look\_up\_name\_get**

> str api\_v1\_look\_up\_name\_get(name=name)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_look_up_name_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->api_v1_look_up_name_get: %s\n" % e)
```

#### Parameters

| Name     | Type    | Description | Notes       |
| -------- | ------- | ----------- | ----------- |
| **name** | **str** |             | \[optional] |

#### Return type

**str**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
