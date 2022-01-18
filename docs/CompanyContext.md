# CompanyContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_records** | **int** | Number of transaction records associated with this company | 
**trading_partners** | **list[str]** | A list of Altana Canonical Company Identifiers, representing the joint set of buyers and suppliers | 
**suppliers** | **list[str]** | A list of Altana Canonical Company Identifiers, representing companies this company buys from | 
**buyers** | **list[str]** | A list of Altana Canonical Company Identifiers, representing companies this company sells to | 
**countries_of_origin** | **list[str]** | A list of ISO-2 country codes | 
**countries_of_destination** | **list[str]** | A list of ISO-2 country codes | 
**countries_of_operation** | **list[str]** | A list of ISO-2 country codes in which a company owns facilities | [optional] 
**hs_traded** | **list[str]** | A list of HS code section prefixes | 
**industries** | **list[str]** | A list of industries defined by Altana taxonomy | 
**products_sent** | **list[str]** | A list of product IDs that a company sends | [optional] 
**products_received** | **list[str]** | A list of product IDs that a company receives | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

