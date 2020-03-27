# This is some example code to pull data from bozemanstrong
# Reference docs at:  https://anvil.works/docs/uplink/data_tables

# first install anvil
# pip install anvil-uplink

import anvil.server
from anvil.tables import app_tables
import dotenv
import os

# we store the client key with dotenv and import as Environment Variables
dotenv.load_dotenv()
ANVILKEY = os.getenv("ANVILCLIENTKEY")

anvil.server.connect(ANVILKEY)

'''
Our Data Table for business listings is called bozeman_business
access the data with the below code

We want "approved=True" so that you're only display data components that have gone through the administrative process
to verify the information

bozeman_business data columns
biz_name :  Business Name
biz_type :  Business Category (dropdown populated in separate table biztype
phone :     Phone Number
website :   URL for business
street :    Street Address
city :      City
zipcode :   Zip Code
hours :     Special Information for their business hours freeform text
details :   Any other additional information they want to provide for their business
delivery :  Boolean : whether they deliver or not
pickup :    Boolean : do they provide curbside pickup etc
giftcard :  Boolean : can you buy a giftcard to support the business at a later time

'''

# gather all columns if it's approved
businesses = app_tables.bozeman_business.search(approved=True)

# businesses is iterable and could easily be fed into either your own database or used as is
print('Bozeman Business Listings')
for biz in businesses:
    print(f"The business name is: {biz['biz_name']}")
print('------------------------------------------')
print('')

print('Business Categories')
# if you wanted to pull all of the possible business types that I use in the dropdown for biz_type
business_types = app_tables.biztype.search()

for item in business_types:
    print(f"{item['description']}")


