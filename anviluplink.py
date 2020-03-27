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


We want "approved=True" so that you're only display data components that have gone through the administrative process
to verify the information

bozeman_business data columns


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


