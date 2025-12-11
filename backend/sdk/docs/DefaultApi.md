# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_car_cars_post**](DefaultApi.md#create_car_cars_post) | **POST** /cars/ | Create Car
[**delete_rental_rentals_rental_id_delete**](DefaultApi.md#delete_rental_rentals_rental_id_delete) | **DELETE** /rentals/{rental_id} | Delete Rental
[**get_car_cars_car_id_get**](DefaultApi.md#get_car_cars_car_id_get) | **GET** /cars/{car_id} | Get Car
[**get_rental_for_car_rentals_car_car_id_get**](DefaultApi.md#get_rental_for_car_rentals_car_car_id_get) | **GET** /rentals/car/{car_id} | Get Rental For Car
[**list_cars_cars_get**](DefaultApi.md#list_cars_cars_get) | **GET** /cars/ | List Cars
[**rent_car_cars_car_id_rent_post**](DefaultApi.md#rent_car_cars_car_id_rent_post) | **POST** /cars/{car_id}/rent | Rent Car


# **create_car_cars_post**
> CarOut create_car_cars_post(car_create)

Create Car

### Example


```python
import openapi_client
from openapi_client.models.car_create import CarCreate
from openapi_client.models.car_out import CarOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    car_create = openapi_client.CarCreate() # CarCreate | 

    try:
        # Create Car
        api_response = api_instance.create_car_cars_post(car_create)
        print("The response of DefaultApi->create_car_cars_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_car_cars_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_create** | [**CarCreate**](CarCreate.md)|  | 

### Return type

[**CarOut**](CarOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rental_rentals_rental_id_delete**
> object delete_rental_rentals_rental_id_delete(rental_id)

Delete Rental

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    rental_id = 56 # int | 

    try:
        # Delete Rental
        api_response = api_instance.delete_rental_rentals_rental_id_delete(rental_id)
        print("The response of DefaultApi->delete_rental_rentals_rental_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_rental_rentals_rental_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rental_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_car_cars_car_id_get**
> CarOut get_car_cars_car_id_get(car_id)

Get Car

### Example


```python
import openapi_client
from openapi_client.models.car_out import CarOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    car_id = 56 # int | 

    try:
        # Get Car
        api_response = api_instance.get_car_cars_car_id_get(car_id)
        print("The response of DefaultApi->get_car_cars_car_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_car_cars_car_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**|  | 

### Return type

[**CarOut**](CarOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rental_for_car_rentals_car_car_id_get**
> RentalOut get_rental_for_car_rentals_car_car_id_get(car_id)

Get Rental For Car

### Example


```python
import openapi_client
from openapi_client.models.rental_out import RentalOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    car_id = 56 # int | 

    try:
        # Get Rental For Car
        api_response = api_instance.get_rental_for_car_rentals_car_car_id_get(car_id)
        print("The response of DefaultApi->get_rental_for_car_rentals_car_car_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_rental_for_car_rentals_car_car_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**|  | 

### Return type

[**RentalOut**](RentalOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cars_cars_get**
> List[CarOut] list_cars_cars_get()

List Cars

### Example


```python
import openapi_client
from openapi_client.models.car_out import CarOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # List Cars
        api_response = api_instance.list_cars_cars_get()
        print("The response of DefaultApi->list_cars_cars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_cars_cars_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CarOut]**](CarOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rent_car_cars_car_id_rent_post**
> RentalOut rent_car_cars_car_id_rent_post(car_id, rent_request)

Rent Car

### Example


```python
import openapi_client
from openapi_client.models.rent_request import RentRequest
from openapi_client.models.rental_out import RentalOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    car_id = 56 # int | 
    rent_request = openapi_client.RentRequest() # RentRequest | 

    try:
        # Rent Car
        api_response = api_instance.rent_car_cars_car_id_rent_post(car_id, rent_request)
        print("The response of DefaultApi->rent_car_cars_car_id_rent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rent_car_cars_car_id_rent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **car_id** | **int**|  | 
 **rent_request** | [**RentRequest**](RentRequest.md)|  | 

### Return type

[**RentalOut**](RentalOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

