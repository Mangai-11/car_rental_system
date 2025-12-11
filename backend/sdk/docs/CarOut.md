# CarOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**make** | **str** |  | 
**model** | **str** |  | 
**year** | **int** |  | 
**daily_rate** | **float** |  | 
**id** | **int** |  | 
**available** | **bool** |  | 

## Example

```python
from openapi_client.models.car_out import CarOut

# TODO update the JSON string below
json = "{}"
# create an instance of CarOut from a JSON string
car_out_instance = CarOut.from_json(json)
# print the JSON string representation of the object
print(CarOut.to_json())

# convert the object into a dict
car_out_dict = car_out_instance.to_dict()
# create an instance of CarOut from a dict
car_out_from_dict = CarOut.from_dict(car_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


