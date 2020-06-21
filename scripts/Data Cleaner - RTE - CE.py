# This is a manual cleaner script for the data. You need to manually change the
# months, years, and occasional details. We will not provide an automated script
# since one should carefully check the data each month to ensure there are no
# holes, weird effects, or others.

# This is the cleaner for the French data from RTE
# https://clients.rte-france.com/lang/an/visiteurs/vie/vie_frequence.jsp

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# # European Data Cleaner
# ## Load Data Sets

# Location of the file
location = r'/PATH/TO/FILE/RTE_Frequence_'
# Year
year = r'2014'
# Month
month = r'10'
month_index = int(month) - 1
# File name
file_name =  year + '_' + month + '.txt'   #

# location to save file and plot
save_to = r'/PATH/TO/STORE/'+year+'/'+month+'/'

# Date ranges
# Check if leap year
if year in ['2008', '2012', '2016', '2020']:
    start_date = [year+'-01-01 00:00:00', year+'-02-01 00:00:00', year+'-03-01 00:00:00', year+'-04-01 00:00:00', year+'-05-01 00:00:00', year+'-06-01 00:00:00', year+'-07-01 00:00:00', year+'-08-01 00:00:00', year+'-09-01 00:00:00', year+'-10-01 00:00:00',year+'-11-01 00:00:00',year+'-12-01 00:00:00' ]
    end_date = [year+'-01-31 23:59:59', year+'-02-29 23:59:59', year+'-03-31 23:59:59', year+'-04-30 23:59:59', year+'-05-31 23:59:59', year+'-06-30 23:59:59', year+'-07-31 23:59:59', year+'-08-31 23:59:59', year+'-09-30 23:59:59', year+'-10-31 23:59:59',year+'-11-30 23:59:59',year+'-12-31 23:59:59' ]
else:
    start_date = [year+'-01-01 00:00:00', year+'-02-01 00:00:00', year+'-03-01 00:00:00', year+'-04-01 00:00:00', year+'-05-01 00:00:00', year+'-06-01 00:00:00', year+'-07-01 00:00:00', year+'-08-01 00:00:00', year+'-09-01 00:00:00', year+'-10-01 00:00:00',year+'-11-01 00:00:00',year+'-12-01 00:00:00' ]
    end_date = [year+'-01-31 23:59:59', year+'-02-28 23:59:59', year+'-03-31 23:59:59', year+'-04-30 23:59:59', year+'-05-31 23:59:59', year+'-06-30 23:59:59', year+'-07-31 23:59:59', year+'-08-31 23:59:59', year+'-09-30 23:59:59', year+'-10-31 23:59:59',year+'-11-30 23:59:59',year+'-12-31 23:59:59' ]

# %%
# read csv files from the source path
df = pd.read_csv(location + file_name, sep=';', engine='python',header=None, skiprows=2, encoding = "ISO-8859-1", skipfooter=1, decimal=',')

# Remove last row
# df.drop(df.tail(1).index,inplace=True)

# Merge dates and times to make a DateTime format. Rename frequency column
df[0] =  pd.to_datetime(df[0])
df = df.drop(columns = [2])
df = df.rename({0:'Time', 1:'Frequency'}, axis='columns')

# If 'INVA' is found on data
#df['Frequency'] = df['Frequency'].apply(lambda x: x.replace('INVA',''))

df['Frequency'] = pd.to_numeric(df['Frequency'])
# Here we remove 50 Hz from the frequency, since it is common to work in a
# reference frame where the nominal frequency is 0 Hz (useful to compare US
# and EU data)
df['Frequency'] = (df['Frequency'] - 50.)*1000 # 60.0 for US and Japan

# use pandas to clean the timeseries.
## First, drop all duplicates entries
df = df.drop_duplicates(subset='Time')

# %%
# There isn't much cleaning possible on the French data, which is sampled at 10
# seconds. The data is very clean and shows no high deviations. Some gaps here
# and there.
fig, ax = plt.subplots(1,1, figsize=(12,3))
ax.plot(df['Frequency'].values, color='black')


from matplotlib.patches import Patch
patch_l = Patch(color='gray', label='Quality of data (impossible to determine)')
fig.text(0.09,0.8, r'Decimals = 1', fontsize=16)
ax.set_ylim([-550,650])
ax.set_yticks([-400,-200,0,200,400])
ax.set_xlabel('Time', fontsize = 18); ax.set_ylabel('F [mHz]', fontsize = 18)
ax.legend(handles=[patch_l], loc=4, ncol=4,fontsize = 14)
fig.subplots_adjust(left=0.07, bottom=0.18, right=.99, top=0.99)
fig.savefig(save_to + year + '_' + month + '.png', dpi = 400, transparent=True)


# %% Save data into a zipped csv. location is save_to
df.to_csv(save_to +year+'_'+month+'.csv.zip', float_format='%.1f',
    compression=dict(method='zip', archive_name=year+'_'+month+'.csv'))
