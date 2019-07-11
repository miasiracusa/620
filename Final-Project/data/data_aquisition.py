# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 23:14:12 2019

@author: JM
"""

'''
The process below was used to obtain OpenSource Data from NYC Socrata API.
'''

# Import python packages
import pandas as pd
from sodapy import Socrata
from socrata_credentials import app_token
 
# Establish connection variables 
domain = "data.cityofnewyork.us"; WRNDB = "pqg4-dm6b"; FAM_VIOL = "a35y-93e7"

# Initiate client connection
client = Socrata(domain = domain, app_token = app_token)

# Obtain results from API request
wrndb = client.get(WRNDB, limit=50000)
fam_viol = client.get(FAM_VIOL, limit=50000)


# Close client connection
client.close()

# Store results in pandas dataframes
wrndb = pd.DataFrame.from_dict(wrndb)
fam_viol = pd.DataFrame.from_dict(fam_viol)

# Write dataframes to csv
wrndb.to_csv(path_or_buf="nyc_wrn_db.csv",index=False)
fam_viol.to_csv(path_or_buf="nyc_fam_viol.csv",index=False)