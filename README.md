# bozemanstrong-exchange
Information for collaborating with the https://bozemanstrong.org website

We leverage the python framework Anvil (more info at https://anvil.works) to accept input and display the data
If there is a special case where sharing that data would be beneficial to the community at large we can do that
levearing an uplink from the Anvil system.  If you are familiar with Python this gives a very simple method to 
iterate through the data.

## Data Usage
Reference docs at:  https://anvil.works/docs/uplink/data_tables

First install anvil's library `pip install anvil-uplink` and refer to anviluplink.py for more implementation details.  Specifically the data tables that are useful are referenced below. Our Data Table for business listings is called **bozeman_business**

Data Column | Data Information (all strings unless specified)
------------|------------------------------------------------
biz_name |  Business Name
biz_type |  Business Category (dropdown populated in separate table biztype
phone |     Phone Number
website |   URL for business
street |    Street Address
city |      City
zipcode |   Zip Code
hours |     Special Information for their business hours freeform text
details |   Any other additional information they want to provide for their business
delivery |  Boolean : whether they deliver or not
pickup |    Boolean : do they provide curbside pickup etc
giftcard |  Boolean : can you buy a giftcard to support the business at a later time

