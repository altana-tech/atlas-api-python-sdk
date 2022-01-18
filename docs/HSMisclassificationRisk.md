# HSMisclassificationRisk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_type** | **str** |  | [optional] 
**risk_score** | **float** |  | [optional] 
**predicted** | [**list[PredictedGoods]**](PredictedGoods.md) |  | [optional] 
**is_declared_hs2_equal_top_1** | **bool** | Returns true if the declared HS code and predicted HS code with the highest confidence have the same first two digits (i.e., HS2) | [optional] 
**is_declared_hs4_equal_top_1** | **bool** | Returns true if the declared HS code and predicted HS code with the highest confidence have the same first four digits (i.e., HS4) | [optional] 
**is_declared_hs6_equal_top_1** | **bool** | Returns true if the declared HS code and predicted HS code with the highest confidence have the same first six digits (i.e., HS6) | [optional] 
**is_declared_hs_equal_top_1** | **bool** | Returns true if the declared HS code and predicted HS code with the highest confidence are the same | [optional] 
**is_declared_hs_in_top_3** | **bool** | Returns true if the declared HS code is one of the top three predicted HS codes, ranked by confidence | [optional] 
**is_declared_hs_in_top_5** | **bool** | Returns true if the declared HS code is one of the top five predicted HS codes, ranked by confidence | [optional] 
**is_tariff_diff_btw_declared_and_top_1** | **bool** | Returns true if the declared HS code and top predicted HS code have different tariff rates associated with them | [optional] 
**top_predicted_confidence** | **float** | Maximum confidence of all predicted HS codes | [optional] 
**mean_predicted_confidence** | **float** | Mean confidence of all predicted HS codes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

