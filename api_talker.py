import numpy as np
import requests
import pandas as pd
from tqdm import tqdm

# from requests.auth import HTTPBasicAuth
OSF_TOKEN = 'tHGlwS8G13M83iFnPpX0JKEfKPFZHTPS10Sfs4a8Gkvbx31uS0QFv3bPHAHGnu4nAXgFk1'
ME = 'https://api.osf.io/v2/users/djgaz/'
headers = {'Authorization': 'Bearer {}'.format(OSF_TOKEN)}


d = pd.DataFrame(columns=['name', 'download'])


def pandafier(block):
  d_ = pd.DataFrame(columns=['name', 'download'])
  for ele in block:
      if ele['attributes']['kind'] == 'file':
          print(ele['attributes']['materialized_path'])
          d_ = d_.append({'name': ele['attributes']['materialized_path'], 'download': ele['links']['download'] },ignore_index=True)

  return d_


# %% Locate folder

nodes = requests.get('https://api.osf.io/v2/nodes/m43tg/files/osfstorage/', headers=headers)

nodes.json()['data']




# %% Upload years

Years = ['2015','2016','2017','2018','2019']

loc = 'https://files.de-1.osf.io/v1/resources/m43tg/providers/osfstorage/5eef6e00145b1a01725326b2/'

# %%
for year in Years:
    requests.put(loc + '?kind=folder&name=' + year, headers=headers)

# %%

nodes = requests.get('https://api.osf.io/v2/nodes/m43tg/files/osfstorage/5ef2565976ebd80262cd75dd/', headers=headers)
nodes.status_code
nodes.json()['data']
loc = nodes.json()['data']

Years = ['2015','2016','2017','2018','2019']
Months = ['01','02','03','04','05','06','07','08','09','10','11','12']


# %%
loc = 'https://files.de-1.osf.io/v1/resources/m43tg/providers/osfstorage/5ef2568b659828023ecf31da/'

for month in Months:
    requests.put(loc + '?kind=folder&name=' + month, headers=headers)


# %%


Years = ['2015','2016','2017','2018','2019']
Months = ['01','02','03','04','05','06','07','08','09','10','11','12']

nodes.json()['data'][0]['relationships']['files']['links']['related']['href']
nodes.json()['data'][0]['attributes']['materialized_path'][-8:-1]

nodes.json()['data']

# %%
# nodes.json()['data']
for ele in tqdm(nodes.json()['data']):
    for sub_elem in requests.get(ele['relationships']['files']['links']['related']['href'], headers=headers).json()['data']:
        # where = sub_elem['attributes']['materialized_path'][-8:]
        # print(where)
        for month in Months:
            requests.put(loc + '?kind=folder&name=' + month, headers=headers)

# %%

base = "/home/leo/Sciebo/Git/Power-Grid-Frequency-Data/Continental Europe/France/"

file =  year + "/" + month + "/" + year + "_" + month + ending
new_file = year + "/" + month + "/" + 'france_' + year + "_" + month + ending


'/home/leo/Sciebo/Git/Power-Grid-Frequency-Data/Continental Europe/France/2020/06/france_2020_06.png'
