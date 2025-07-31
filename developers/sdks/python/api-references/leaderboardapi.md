# LeaderboardApi

## swagger\_client.LeaderboardApi

All URIs are relative to _/_

| Method                             | HTTP request                   | Description |
| ---------------------------------- | ------------------------------ | ----------- |
| **api\_v1\_get\_leaderboard\_get** | **GET** /api/v1/GetLeaderboard |             |

## **api\_v1\_get\_leaderboard\_get**

> LeaderboardResult api\_v1\_get\_leaderboard\_get(name=name)

#### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeaderboardApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.api_v1_get_leaderboard_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardApi->api_v1_get_leaderboard_get: %s\n" % e)
```

#### Parameters

| Name     | Type    | Description | Notes       |
| -------- | ------- | ----------- | ----------- |
| **name** | **str** |             | \[optional] |

#### Return type

**LeaderboardResult**

#### Authorization

No authorization required

#### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

[\[Back to top\]](broken-reference) \[Back to API list] \[Back to Model list] \[Back to README]
