# ContractApi

## swagger\_client.ContractApi

All URIs are relative to _/_

| Method                                       | HTTP request                         | Description |
| -------------------------------------------- | ------------------------------------ | ----------- |
| **api\_v1\_get\_contract\_by\_address\_get** | **GET** /api/v1/GetContractByAddress |             |
| **api\_v1\_get\_contract\_get**              | **GET** /api/v1/GetContract          |             |

## **api\_v1\_get\_contract\_by\_address\_get**

> ContractResult api\_v1\_get\_contract\_by\_address\_get(chain\_address\_or\_name=chain\_address\_or\_name, contract\_address=contract\_address)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
contract_address = 'contract_address_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_contract_by_address_get(chain_address_or_name=chain_address_or_name, contract_address=contract_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->api_v1_get_contract_by_address_get: %s\n" % e)
```

#### Parameters

| Name                         | Type    | Description | Notes       |
| ---------------------------- | ------- | ----------- | ----------- |
| **chain\_address\_or\_name** | **str** |             | \[optional] |
| **contract\_address**        | **str** |             | \[optional] |

#### Return type

**ContractResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_contract\_get**

> ContractResult api\_v1\_get\_contract\_get(chain\_address\_or\_name=chain\_address\_or\_name, contract\_name=contract\_name)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContractApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
contract_name = 'contract_name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_contract_get(chain_address_or_name=chain_address_or_name, contract_name=contract_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContractApi->api_v1_get_contract_get: %s\n" % e)
```

#### Parameters

| Name                         | Type    | Description | Notes       |
| ---------------------------- | ------- | ----------- | ----------- |
| **chain\_address\_or\_name** | **str** |             | \[optional] |
| **contract\_name**           | **str** |             | \[optional] |

#### Return type

**ContractResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
