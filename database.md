---
Title: Database

menus:
  main:
    weight: 1
    title: Database
layout: single
toc: true
toc_label: "Database"
toc_icon: "cog"
---

The target is to collect, process, and document all available power-grid frequency data publicly available and make it research ready.

# Publicly available data from TSOs

The links are direct downloads. Each is a zipped csv `.csv.zip` file. In [Power-Grid-Frequency](https://github.com/LRydin/Power-Grid-Frequency/tree/master/Data) and each respective subfolder you can find a plot for each month of the processed data with some details of the data processing and the quality of the actual data.

_Data structure_

The data is structured in two columns: first column is a data-time format, e.g. `2017-01-01 00:00:00`. The second column is the frequency deviation from the reference in mHz, e.g. `44.006`.

To read the data directly in `python`, use `pandas` as

```python
import pandas as pd
df = pd.read_csv('path/to/germany_2017_01.csv.zip', index_col=0)
```

`pandas` is smart enough to unzip the `.csv` and read it.

## Continental Europe

### Germany

{% include_relative /Data/Continental-Europe/Germany/readme.md %}

### France

{% include_relative /Data/Continental-Europe/France/readme.md %}

## Nordic Grid

### Finland

{% include_relative /Data/Nordic-Grid/Finland/readme.md %}

## National Grid

### Great Britain

{% include_relative /Data/National-Grid/Great-Britain/readme.md %}

# Research projects open data

## Power grid frequency data base

{% include_relative /Data/Research-Projects/Power-grid-frequency-data-base/readme.md %}

## Aces

### Denmark, Continental Europe

{% include_relative /Data/Research-Projects/ACES/Denmark/readmeCE.md %}

### Denmark, Nordic Grid

{% include_relative /Data/Research-Projects/ACES/Denmark/readmeNG.md %}

### Japan, Japanese 50Hz Grid

{% include_relative /Data/Research-Projects/ACES/Japan/Japanese50Hz/readmeJapan.md %}

# Independent measurements

## Continental Europe

### Hungary

{% include_relative /Data/Research-Projects/Hungary/readme.md %}

## Nordic Grid

### Sweden

{% include_relative /Data/Nordic-Grid/Sweden/readme.md%}
