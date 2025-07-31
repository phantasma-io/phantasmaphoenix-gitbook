# AuctionApi

## swagger\_client.AuctionApi

All URIs are relative to _/_

| Method                                 | HTTP request                     | Description |
| -------------------------------------- | -------------------------------- | ----------- |
| **api\_v1\_get\_auction\_get**         | **GET** /api/v1/GetAuction       |             |
| **api\_v1\_get\_auctions\_count\_get** | **GET** /api/v1/GetAuctionsCount |             |
| **api\_v1\_get\_auctions\_get**        | **GET** /api/v1/GetAuctions      |             |

## **api\_v1\_get\_auction\_get**

> AuctionResult api\_v1\_get\_auction\_get(chain\_address\_or\_name=chain\_address\_or\_name, symbol=symbol, i\_dtext=i\_dtext)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
symbol = 'symbol_example' # str |  (optional)
i_dtext = 'i_dtext_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_auction_get(chain_address_or_name=chain_address_or_name, symbol=symbol, i_dtext=i_dtext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->api_v1_get_auction_get: %s\n" % e)
```

#### Parameters

| Name                         | Type    | Description | Notes       |
| ---------------------------- | ------- | ----------- | ----------- |
| **chain\_address\_or\_name** | **str** |             | \[optional] |
| **symbol**                   | **str** |             | \[optional] |
| **i\_dtext**                 | **str** |             | \[optional] |

#### Return type

**AuctionResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_auctions\_count\_get**

> int api\_v1\_get\_auctions\_count\_get(chain\_address\_or\_name=chain\_address\_or\_name, symbol=symbol)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
symbol = 'symbol_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_auctions_count_get(chain_address_or_name=chain_address_or_name, symbol=symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->api_v1_get_auctions_count_get: %s\n" % e)
```

#### Parameters

| Name                         | Type    | Description | Notes       |
| ---------------------------- | ------- | ----------- | ----------- |
| **chain\_address\_or\_name** | **str** |             | \[optional] |
| **symbol**                   | **str** |             | \[optional] |

#### Return type

**int**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_auctions\_get**

> PaginatedResult api\_v1\_get\_auctions\_get(chain\_address\_or\_name=chain\_address\_or\_name, symbol=symbol, page=page, page\_size=page\_size)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuctionApi()
chain_address_or_name = 'chain_address_or_name_example' # str |  (optional)
symbol = 'symbol_example' # str |  (optional)
page = 1 # int |  (optional) (default to 1)
page_size = 99999 # int |  (optional) (default to 99999)

try:
    api_response = api_instance.api_v1_get_auctions_get(chain_address_or_name=chain_address_or_name, symbol=symbol, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuctionApi->api_v1_get_auctions_get: %s\n" % e)
```

#### Parameters

| Name                         | Type    | Description | Notes                           |
| ---------------------------- | ------- | ----------- | ------------------------------- |
| **chain\_address\_or\_name** | **str** |             | \[optional]                     |
| **symbol**                   | **str** |             | \[optional]                     |
| **page**                     | **int** |             | \[optional] \[default to 1]     |
| **page\_size**               | **int** |             | \[optional] \[default to 99999] |

#### Return type

**PaginatedResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
