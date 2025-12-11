# RentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 

## Example

```python
from openapi_client.models.rent_request import RentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RentRequest from a JSON string
rent_request_instance = RentRequest.from_json(json)
# print the JSON string representation of the object
print(RentRequest.to_json())

# convert the object into a dict
rent_request_dict = rent_request_instance.to_dict()
# create an instance of RentRequest from a dict
rent_request_from_dict = RentRequest.from_dict(rent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


