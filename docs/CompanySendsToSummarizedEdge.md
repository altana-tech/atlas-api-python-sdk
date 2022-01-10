# CompanySendsToSummarizedEdge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_sends_to_summarized_id** | **str** | A unique identifier for a company sends to summarized edge | [optional] 
**country_of_destination_summary** | [**list[CountryCount]**](CountryCount.md) | A list of dictionaries of country of destination ALPHA ISO-2 codes to transaction counts | [optional] 
**country_of_origin_summary** | [**list[CountryCount]**](CountryCount.md) | A list of dictionaries of country of origin ALPHA ISO-2 codes to transaction counts | [optional] 
**destination_id** | **str** | The company_canon_id of the destination company | [optional] 
**hs_codes_sent** | [**list[HSCodeCount]**](HSCodeCount.md) | A list of dictionaries of the HS codes of sent goods to transaction counts | [optional] 
**number_of_shipments** | **int** | The number of shipments represented by the summarized edge | [optional] 
**source_id** | **str** | The company_canon_id of the source company | [optional] 
**sources** | **list[str]** | A list of data sources for the information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

