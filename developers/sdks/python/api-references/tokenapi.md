# TokenApi

## swagger\_client.TokenApi

All URIs are relative to _/_

| Method                                | HTTP request                    | Description |
| ------------------------------------- | ------------------------------- | ----------- |
| **api\_v1\_get\_nft\_get**            | **GET** /api/v1/GetNFT          |             |
| **api\_v1\_get\_nfts\_get**           | **GET** /api/v1/GetNFTs         |             |
| **api\_v1\_get\_token\_balance\_get** | **GET** /api/v1/GetTokenBalance |             |
| **api\_v1\_get\_token\_data\_get**    | **GET** /api/v1/GetTokenData    |             |
| **api\_v1\_get\_token\_get**          | **GET** /api/v1/GetToken        |             |
| **api\_v1\_get\_tokens\_get**         | **GET** /api/v1/GetTokens       |             |

## **api\_v1\_get\_nft\_get**

> TokenDataResult api\_v1\_get\_nft\_get(symbol=symbol, i\_dtext=i\_dtext, extended=extended)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
i_dtext = 'i_dtext_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_nft_get(symbol=symbol, i_dtext=i_dtext, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_nft_get: %s\n" % e)
```

#### Parameters

| Name         | Type     | Description | Notes                           |
| ------------ | -------- | ----------- | ------------------------------- |
| **symbol**   | **str**  |             | \[optional]                     |
| **i\_dtext** | **str**  |             | \[optional]                     |
| **extended** | **bool** |             | \[optional] \[default to false] |

#### Return type

**TokenDataResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_nfts\_get**

> list\[TokenDataResult] api\_v1\_get\_nfts\_get(symbol=symbol, id\_text=id\_text, extended=extended)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
id_text = 'id_text_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_nfts_get(symbol=symbol, id_text=id_text, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_nfts_get: %s\n" % e)
```

#### Parameters

| Name         | Type     | Description | Notes                           |
| ------------ | -------- | ----------- | ------------------------------- |
| **symbol**   | **str**  |             | \[optional]                     |
| **id\_text** | **str**  |             | \[optional]                     |
| **extended** | **bool** |             | \[optional] \[default to false] |

#### Return type

**list\[TokenDataResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_token\_balance\_get**

> BalanceResult api\_v1\_get\_token\_balance\_get(account=account, token\_symbol=token\_symbol, chain\_input=chain\_input)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
account = 'account_example' # str |  (optional)
token_symbol = 'token_symbol_example' # str |  (optional)
chain_input = 'chain_input_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_token_balance_get(account=account, token_symbol=token_symbol, chain_input=chain_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_token_balance_get: %s\n" % e)
```

#### Parameters

| Name              | Type    | Description | Notes       |
| ----------------- | ------- | ----------- | ----------- |
| **account**       | **str** |             | \[optional] |
| **token\_symbol** | **str** |             | \[optional] |
| **chain\_input**  | **str** |             | \[optional] |

#### Return type

**BalanceResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_token\_data\_get**

> TokenDataResult api\_v1\_get\_token\_data\_get(symbol=symbol, i\_dtext=i\_dtext)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
i_dtext = 'i_dtext_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_token_data_get(symbol=symbol, i_dtext=i_dtext)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_token_data_get: %s\n" % e)
```

#### Parameters

| Name         | Type    | Description | Notes       |
| ------------ | ------- | ----------- | ----------- |
| **symbol**   | **str** |             | \[optional] |
| **i\_dtext** | **str** |             | \[optional] |

#### Return type

**TokenDataResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_token\_get**

> TokenResult api\_v1\_get\_token\_get(symbol=symbol, extended=extended)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
symbol = 'symbol_example' # str |  (optional)
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_token_get(symbol=symbol, extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_token_get: %s\n" % e)
```

#### Parameters

| Name         | Type     | Description | Notes                           |
| ------------ | -------- | ----------- | ------------------------------- |
| **symbol**   | **str**  |             | \[optional]                     |
| **extended** | **bool** |             | \[optional] \[default to false] |

#### Return type

**TokenResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]

## **api\_v1\_get\_tokens\_get**

> list\[TokenResult] api\_v1\_get\_tokens\_get(extended=extended)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TokenApi()
extended = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.api_v1_get_tokens_get(extended=extended)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->api_v1_get_tokens_get: %s\n" % e)
```

#### Parameters

| Name         | Type     | Description | Notes                           |
| ------------ | -------- | ----------- | ------------------------------- |
| **extended** | **bool** |             | \[optional] \[default to false] |

#### Return type

**list\[TokenResult]**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
