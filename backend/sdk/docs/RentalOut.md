# RentalOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**car_id** | **int** |  | 
**user_name** | **str** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**rental_date** | **datetime** |  | 

## Example

```python
from openapi_client.models.rental_out import RentalOut

# TODO update the JSON string below
json = "{}"
# create an instance of RentalOut from a JSON string
rental_out_instance = RentalOut.from_json(json)
# print the JSON string representation of the object
print(RentalOut.to_json())

# convert the object into a dict
rental_out_dict = rental_out_instance.to_dict()
# create an instance of RentalOut from a dict
rental_out_from_dict = RentalOut.from_dict(rental_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


