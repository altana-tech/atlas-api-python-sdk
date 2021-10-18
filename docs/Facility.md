# Facility

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_canon_id** | **str** | Altana generated, entity resolved UUID representing a facility | [optional] 
**company_canon_id** | **str** | Altana generated, entity resolved UUID representing a company | [optional] 
**company_name** | **str** | The resolved company name associated with the company canon ID | [optional] 
**hs_received** | **list[str]** | A list of HS codes that the facility has received | [optional] 
**hs_sent** | **list[str]** | A list of HS codes that the facility has sent | [optional] 
**hs_traded** | **list[str]** | A list of HS codes that the facility has traded (i.e. sent and received) | [optional] 
**receives_from_facility_ids** | **list[str]** | A list of facility IDs that this facility receives products from | [optional] 
**sends_to_facility_ids** | **list[str]** | A list of facility IDs that this facility sends products to | [optional] 
**address** | **str** | The address of this facility | [optional] 
**coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] 
**restrictions** | [**list[Restriction]**](Restriction.md) |  | [optional] 
**industries** | **list[str]** | A list of industries defined by Altana taxonomy | [optional] 
**number_records** | **int** | Number of transaction records associated with this facility | [optional] 
**data_sources** | **list[str]** |  | [optional] 
**products_sent** | **list[str]** | A list of product IDs that a facility sends | [optional] 
**products_received** | **list[str]** | A list of product IDs that a facility receives | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

