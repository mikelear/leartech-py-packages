# leartech_blockchain_api.BlockchainApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_chain_status_get**](BlockchainApi.md#api_v1_chain_status_get) | **GET** /api/v1/chain/status | Chain status
[**api_v1_contracts_address_read_post**](BlockchainApi.md#api_v1_contracts_address_read_post) | **POST** /api/v1/contracts/{address}/read | Call a view/pure method on a contract
[**api_v1_contracts_get**](BlockchainApi.md#api_v1_contracts_get) | **GET** /api/v1/contracts | List known contracts
[**api_v1_deployments_get**](BlockchainApi.md#api_v1_deployments_get) | **GET** /api/v1/deployments | Get contract deployments
[**api_v1_events_get**](BlockchainApi.md#api_v1_events_get) | **GET** /api/v1/events | Get contract events
[**api_v1_transactions_hash_get**](BlockchainApi.md#api_v1_transactions_hash_get) | **GET** /api/v1/transactions/{hash} | Get a transaction by hash


# **api_v1_chain_status_get**
> BlockchainChainStatus api_v1_chain_status_get()

Chain status

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_blockchain_api
from leartech_blockchain_api.models.blockchain_chain_status import BlockchainChainStatus
from leartech_blockchain_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_blockchain_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_blockchain_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_blockchain_api.BlockchainApi(api_client)

    try:
        # Chain status
        api_response = await api_instance.api_v1_chain_status_get()
        print("The response of BlockchainApi->api_v1_chain_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->api_v1_chain_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BlockchainChainStatus**](BlockchainChainStatus.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_contracts_address_read_post**
> BlockchainReadResult api_v1_contracts_address_read_post(address, body)

Call a view/pure method on a contract

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_blockchain_api
from leartech_blockchain_api.models.blockchain_read_result import BlockchainReadResult
from leartech_blockchain_api.models.handlers_read_contract_request import HandlersReadContractRequest
from leartech_blockchain_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_blockchain_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_blockchain_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_blockchain_api.BlockchainApi(api_client)
    address = 'address_example' # str | deployed contract address
    body = leartech_blockchain_api.HandlersReadContractRequest() # HandlersReadContractRequest | method + args

    try:
        # Call a view/pure method on a contract
        api_response = await api_instance.api_v1_contracts_address_read_post(address, body)
        print("The response of BlockchainApi->api_v1_contracts_address_read_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->api_v1_contracts_address_read_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| deployed contract address | 
 **body** | [**HandlersReadContractRequest**](HandlersReadContractRequest.md)| method + args | 

### Return type

[**BlockchainReadResult**](BlockchainReadResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_contracts_get**
> HandlersListResponse api_v1_contracts_get(name=name, kind=kind)

List known contracts

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_blockchain_api
from leartech_blockchain_api.models.handlers_list_response import HandlersListResponse
from leartech_blockchain_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_blockchain_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_blockchain_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_blockchain_api.BlockchainApi(api_client)
    name = 'name_example' # str | filter by contract name (optional)
    kind = 'kind_example' # str | filter by contract kind (e.g. oracle, consumer) (optional)

    try:
        # List known contracts
        api_response = await api_instance.api_v1_contracts_get(name=name, kind=kind)
        print("The response of BlockchainApi->api_v1_contracts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->api_v1_contracts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| filter by contract name | [optional] 
 **kind** | **str**| filter by contract kind (e.g. oracle, consumer) | [optional] 

### Return type

[**HandlersListResponse**](HandlersListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_deployments_get**
> HandlersListResponse api_v1_deployments_get(contract=contract, chain=chain, address=address)

Get contract deployments

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_blockchain_api
from leartech_blockchain_api.models.handlers_list_response import HandlersListResponse
from leartech_blockchain_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_blockchain_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_blockchain_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_blockchain_api.BlockchainApi(api_client)
    contract = 'contract_example' # str | filter by contract name (optional)
    chain = 'chain_example' # str | filter by chain (optional)
    address = 'address_example' # str | filter by deployed address (optional)

    try:
        # Get contract deployments
        api_response = await api_instance.api_v1_deployments_get(contract=contract, chain=chain, address=address)
        print("The response of BlockchainApi->api_v1_deployments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->api_v1_deployments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| filter by contract name | [optional] 
 **chain** | **str**| filter by chain | [optional] 
 **address** | **str**| filter by deployed address | [optional] 

### Return type

[**HandlersListResponse**](HandlersListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_events_get**
> HandlersListResponse api_v1_events_get(address=address, event=event, from_block=from_block, to_block=to_block, tx_hash=tx_hash)

Get contract events

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_blockchain_api
from leartech_blockchain_api.models.handlers_list_response import HandlersListResponse
from leartech_blockchain_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_blockchain_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_blockchain_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_blockchain_api.BlockchainApi(api_client)
    address = 'address_example' # str | filter by contract address (optional)
    event = 'event_example' # str | filter by event name (optional)
    from_block = 56 # int | first block (inclusive) (optional)
    to_block = 56 # int | last block (inclusive) (optional)
    tx_hash = 'tx_hash_example' # str | filter by transaction hash (optional)

    try:
        # Get contract events
        api_response = await api_instance.api_v1_events_get(address=address, event=event, from_block=from_block, to_block=to_block, tx_hash=tx_hash)
        print("The response of BlockchainApi->api_v1_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->api_v1_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| filter by contract address | [optional] 
 **event** | **str**| filter by event name | [optional] 
 **from_block** | **int**| first block (inclusive) | [optional] 
 **to_block** | **int**| last block (inclusive) | [optional] 
 **tx_hash** | **str**| filter by transaction hash | [optional] 

### Return type

[**HandlersListResponse**](HandlersListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_transactions_hash_get**
> BlockchainTransaction api_v1_transactions_hash_get(hash)

Get a transaction by hash

### Example

* Api Key Authentication (BearerAuth):

```python
import leartech_blockchain_api
from leartech_blockchain_api.models.blockchain_transaction import BlockchainTransaction
from leartech_blockchain_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = leartech_blockchain_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with leartech_blockchain_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leartech_blockchain_api.BlockchainApi(api_client)
    hash = 'hash_example' # str | transaction hash

    try:
        # Get a transaction by hash
        api_response = await api_instance.api_v1_transactions_hash_get(hash)
        print("The response of BlockchainApi->api_v1_transactions_hash_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainApi->api_v1_transactions_hash_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| transaction hash | 

### Return type

[**BlockchainTransaction**](BlockchainTransaction.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

