# This is a manual cleaner script for the data. You need to manually change the
# months, years, and occasional details. We will not provide an automated script
# since one should carefully check the data each month to ensure there are no
# holes, weird effects, or others.

# This is the Cleaner for the German data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# # European Data Cleaner
# ## Load Data Sets

# Location of the file: assuming it is named as year_month_Frequenz.csv
location = r'/PATH/TO/FILE/'
# Year
year = r'2014'
# Month
month = r'12'
month_index = int(month) - 1
# File name
file_name = year + '_'+ month +  '/'+ year + month + '_Frequenz.csv'

# location to save file and plot
save_to = r'/PATH/TO/STORE/'+year+'/'+month+'/'

# Date ranges
# Check if leap year
if year in ['2008', '2012', '2016', '2020']:
    start_date = [year+'-01-01 00:00:00', year+'-02-01 00:00:00', year+'-03-01 00:00:00', year+'-04-01 00:00:00', year+'-05-01 00:00:00', year+'-06-01 00:00:00', year+'-07-01 00:00:00', year+'-08-01 00:00:00', year+'-09-01 00:00:00', year+'-10-01 00:00:00',year+'-11-01 00:00:00',year+'-12-01 00:00:00' ]
    end_date = [year+'-01-31 23:59:59', year+'-02-28 23:59:59', year+'-03-31 23:59:59', year+'-04-30 23:59:59', year+'-05-31 23:59:59', year+'-06-30 23:59:59', year+'-07-31 23:59:59', year+'-08-31 23:59:59', year+'-09-30 23:59:59', year+'-10-31 23:59:59',year+'-11-30 23:59:59',year+'-12-31 23:59:59' ]
else:
    start_date = [year+'-01-01 00:00:00', year+'-02-01 00:00:00', year+'-03-01 00:00:00', year+'-04-01 00:00:00', year+'-05-01 00:00:00', year+'-06-01 00:00:00', year+'-07-01 00:00:00', year+'-08-01 00:00:00', year+'-09-01 00:00:00', year+'-10-01 00:00:00',year+'-11-01 00:00:00',year+'-12-01 00:00:00' ]
    end_date = [year+'-01-31 23:59:59', year+'-02-27 23:59:59', year+'-03-31 23:59:59', year+'-04-30 23:59:59', year+'-05-31 23:59:59', year+'-06-30 23:59:59', year+'-07-31 23:59:59', year+'-08-31 23:59:59', year+'-09-30 23:59:59', year+'-10-31 23:59:59',year+'-11-30 23:59:59',year+'-12-31 23:59:59' ]

# %%
#read csv files from the source path
df = pd.read_csv(location + file_name, sep=',',header=None)

# Adjust for daylight savings by removing an hour in October. It produces an
# waring in python 3.7.
# df[1][2174400-2*3600:2174400-1*3600] = list(map(str,pd.date_range('02:00:00','02:59:59', freq = 'S').time))
# df = df.drop(df.index[2174400-1*3600:2174400-0*3600])

# Merge dates and times to make a DateTime format. Rename frequency column
df[0] =  pd.to_datetime(df[0] + ' ' + df[1])
df = df.drop(columns = [1,2])
df = df.rename({0:'Time', 3:'Frequency'}, axis='columns')


# Here we remove 50 Hz from the frequency, since it is common to work in a
# reference frame where the nominal frequency is 0 Hz (useful to compare US
# and EU data)
df['Frequency'] = (df['Frequency'] - 50.)*1000 # 60.0 for US and Japan

# use pandas to clean the timeseries.
## First, drop all duplicates entries
df = df.drop_duplicates(subset='Time')
df
## Now ensure the first entry is the first second of the month and the last
## the last second of the month.

idx = pd.date_range(start_date[month_index], end_date[month_index], freq = 'S')
df = df.set_index('Time').rename_axis(None)
df = df.reindex(idx, fill_value=np.nan)

# %% Plot a 'quality plot' with the jumps, fluctuations and dead zones
fig, ax = plt.subplots(1,1, figsize=(12,3))
ax.plot(df['Frequency'], color='black')
ax.plot(df[df['Frequency'] > 1000], 'o', color = 'darkblue', label = r'|F|>1000')
ax.plot(df[df['Frequency'] < -1000], 'o', color = 'darkblue')
ax.plot(df[df['Frequency'].diff() > 30], 'o', color = 'darkorange', label = r"|F'|>30")
ax.plot(df[df['Frequency'].diff() < -30], 'o', color = 'darkorange')
df.index
cond = df.diff()==0

for c in df.columns:
    grouper = (cond[c] != cond[c].shift(1)).cumsum() * cond[c]
    fill = (df.groupby(grouper)[c].transform('size') >= 20)
    filter = fill & cond['Frequency']
    tr1 = np.ma.masked_where(filter == False, filter)
    l3 = ax.fill_between(df.index, tr1*0-500, tr1*0+500, color = 'purple', alpha=0.3, label = r'Plateaus F>20s');
    for j in tqdm(range((df.index[-1] - df.index[0]).days +1)):
        for i in range(2,20):
            temp[i-2] = (((df.groupby(grouper)[c].transform('size') == i) & cond['Frequency'])[n*(j):n*(j+1)].sum()/float(i)) / (n/(float(i)+1))
        filters[j,:] = temp
        ax.fill_between(df.index[n*(j):n*(j+1)], np.ones_like(n) +530, np.ones_like(n)+600, color = greyish(np.sum(temp)), alpha=1, facecolor="none");

from matplotlib.patches import Patch
patch_l = Patch(color='gray', label='Quality of data (impossible to determine)')
fig.text(0.09,0.8, r'Decimals = 0', fontsize=16)
ax.set_ylim([-550,650])
ax.set_yticks([-400,-200,0,200,400])
ax.set_xlabel('Time', fontsize = 18); ax.set_ylabel('F [mHz]', fontsize = 18)
ax.legend(handles=[l1[0],l2[0], l3, patch_l], loc=4, ncol=4,fontsize = 14)
fig.subplots_adjust(left=0.07, bottom=0.18, right=.99, top=0.99)
fig.savefig(save_to + year+'_'+month + '.png', dpi = 400, transparent=True)
np.savez_compressed(save_to+ 'Data_from_cleaning_' + year+'_'+month, filters=filters, cond=cond)

# %% Now actually clean the encountered bogus recording. Set all errors to NaN
df[df['Frequency'] > 1000] = np.nan
df[df['Frequency'] < -1000] = np.nan
df[df['Frequency'].diff() > 20] = np.nan
df[df['Frequency'].diff() < -20] = np.nan
df['Frequency'].isna().sum()

# Find plateaus of length > 10 and replace by NaN
cond = df.diff()==0

for c in df.columns:
    grouper = (cond[c] != cond[c].shift(1)).cumsum() * cond[c]
    fill = (df.groupby(grouper)[c].transform('size') >= 20)
    df.loc[fill & cond[c], c] = np.nan

# %% Save data into a zipped csv. location is save_to

df.to_csv(save_to +year+'_'+month+'.csv.zip', float_format='%.3f',
    compression=dict(method='zip', archive_name=year+'_'+month+'.csv'))


# %% Extras: Removing the extra hour in October due to daylight savings
## 2014
# df[1][2174400-2*3600:2174400-1*3600] = list(map(str,pd.date_range('02:00:00','02:59:59', freq = 'S').time))
# df = df.drop(df.index[2174400-1*3600:2174400-0*3600])
