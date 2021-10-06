# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_item_items_item_id_get**](DefaultApi.md#read_item_items_item_id_get) | **GET** /items/{item_id} | Read Item
[**read_root_get**](DefaultApi.md#read_root_get) | **GET** / | Read Root

# **read_item_items_item_id_get**
> object read_item_items_item_id_get(item_id, q=q)

Read Item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
item_id = 56 # int | 
q = 'q_example' # str |  (optional)

try:
    # Read Item
    api_response = api_instance.read_item_items_item_id_get(item_id, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_item_items_item_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**|  | 
 **q** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_root_get**
> object read_root_get()

Read Root

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Read Root
    api_response = api_instance.read_root_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_root_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

