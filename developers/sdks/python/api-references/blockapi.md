# BlockApi

## swagger\_client.BlockApi

All URIs are relative to _/_

| Method                                                     | HTTP request                                   | Description |
| ---------------------------------------------------------- | ---------------------------------------------- | ----------- |
| **api\_v1\_get\_block\_by\_hash\_get**                     | **GET** /api/v1/GetBlockByHash                 |             |
| **api\_v1\_get\_block\_by\_height\_get**                   | **GET** /api/v1/GetBlockByHeight               |             |
| **api\_v1\_get\_block\_height\_get**                       | **GET** /api/v1/GetBlockHeight                 |             |
| **api\_v1\_get\_block\_transaction\_count\_by\_hash\_get** | **GET** /api/v1/GetBlockTransactionCountByHash |             |
| **api\_v1\_get\_latest\_block\_get**                       | **GET** /api/v1/GetLatestBlock                 |             |
| **api\_v1\_get\_raw\_block\_by\_hash\_get**                | **GET** /api/v1/GetRawBlockByHash              |             |
| **api\_v1\_get\_raw\_block\_by\_height\_get**              | **GET** /api/v1/GetRawBlockByHeight            |             |
| **api\_v1\_get\_raw\_latest\_block\_get**                  | **GET** /api/v1/GetRawLatestBlock              |             |

## **api\_v1\_get\_block\_by\_hash\_get**

> BlockResult api\_v1\_get\_block\_by\_hash\_get(block\_hash=block\_hash)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
block_hash = 'block_hash_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_by_hash_get(block_hash=block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_by_hash_get: %s\n" % e)
```

#### Parameters

| Name            | Type    | Description | Notes       |
| --------------- | ------- | ----------- | ----------- |
| **block\_hash** | **str** |             | \[optional] |

#### Return type

**BlockResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_block\_by\_height\_get**

> BlockResult api\_v1\_get\_block\_by\_height\_get(chain\_input=chain\_input, height=height)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)
height = 'height_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_by_height_get(chain_input=chain_input, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_by_height_get: %s\n" % e)
```

#### Parameters

| Name             | Type    | Description | Notes       |
| ---------------- | ------- | ----------- | ----------- |
| **chain\_input** | **str** |             | \[optional] |
| **height**       | **str** |             | \[optional] |

#### Return type

**BlockResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_block\_height\_get**

> str api\_v1\_get\_block\_height\_get(chain\_input=chain\_input)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_height_get(chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_height_get: %s\n" % e)
```

#### Parameters

| Name             | Type    | Description | Notes       |
| ---------------- | ------- | ----------- | ----------- |
| **chain\_input** | **str** |             | \[optional] |

#### Return type

**str**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_block\_transaction\_count\_by\_hash\_get**

> int api\_v1\_get\_block\_transaction\_count\_by\_hash\_get(chain\_address\_or\_name=chain\_address\_or\_name, block\_hash=block\_hash)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
block_hash = 'block_hash_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_block_transaction_count_by_hash_get(chain_address_or_name=chain_address_or_name, block_hash=block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_block_transaction_count_by_hash_get: %s\n" % e)
```

#### Parameters

| Name                         | Type    | Description | Notes       |
| ---------------------------- | ------- | ----------- | ----------- |
| **chain\_address\_or\_name** | **str** |             | \[optional] |
| **block\_hash**              | **str** |             | \[optional] |

#### Return type

**int**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_latest\_block\_get**

> BlockResult api\_v1\_get\_latest\_block\_get(chain\_input=chain\_input)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_latest_block_get(chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_latest_block_get: %s\n" % e)
```

#### Parameters

| Name             | Type    | Description | Notes       |
| ---------------- | ------- | ----------- | ----------- |
| **chain\_input** | **str** |             | \[optional] |

#### Return type

**BlockResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_raw\_block\_by\_hash\_get**

> str api\_v1\_get\_raw\_block\_by\_hash\_get(block\_hash=block\_hash)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
block_hash = 'block_hash_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_raw_block_by_hash_get(block_hash=block_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_raw_block_by_hash_get: %s\n" % e)
```

#### Parameters

| Name            | Type    | Description | Notes       |
| --------------- | ------- | ----------- | ----------- |
| **block\_hash** | **str** |             | \[optional] |

#### Return type

**str**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_raw\_block\_by\_height\_get**

> str api\_v1\_get\_raw\_block\_by\_height\_get(chain\_input=chain\_input, height=height)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)
height = 'height_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_raw_block_by_height_get(chain_input=chain_input, height=height)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_raw_block_by_height_get: %s\n" % e)
```

#### Parameters

| Name             | Type    | Description | Notes       |
| ---------------- | ------- | ----------- | ----------- |
| **chain\_input** | **str** |             | \[optional] |
| **height**       | **str** |             | \[optional] |

#### Return type

**str**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_raw\_latest\_block\_get**

> str api\_v1\_get\_raw\_latest\_block\_get(chain\_input=chain\_input)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BlockApi()
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_raw_latest_block_get(chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockApi->api_v1_get_raw_latest_block_get: %s\n" % e)
```

#### Parameters

| Name             | Type    | Description | Notes       |
| ---------------- | ------- | ----------- | ----------- |
| **chain\_input** | **str** |             | \[optional] |

#### Return type

**str**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
