# Power-Grid Frequency

Power-grid frequency data from around the world, cleaned and processed for research usage.

The data is collected from the TSO's and is processed to remove dead recordings, spikes, and other naturally assumed bad measurements. The scripts that are used to clean the data are also included, for transparency.

# European Grids

The available recordings from Europe are of the following synchronous regions

 - Continental Europe:
   - Germany [1 sec recordings] - [TransnetBW](https://www.transnetbw.com/en/energy-market/ancillary-services/control-reserve-demand-activation)
   - Germany [1 sec recordings] - [50hertz](https://www.50hertz.com/de/) - currently not working
   - France [10 sec recordings]- [RTE](https://clients.rte-france.com/lang/an/visiteurs/vie/vie_frequence.jsp)

 - Nordic Grid:
   - Finland [0.1 sec recordings] - [FinGrid](https://data.fingrid.fi/en/dataset/frequency-historical-data)

 - Great Britain:
   - England [1 sec recordings] - [NationalGrid ESO](https://www.nationalgrideso.com/balancing-services/frequency-response-services/historic-frequency-data)


## Available data

|   | Germany | France | Great Britain | Nordic Grid |
|:-----:|:------------------:|:---:|:---:|:---:|
| 2019  | :heavy_check_mark: | :x: | :x: | :x: |
| 2018  | :heavy_check_mark: | :x: | :x: | :x: |
| 2017  | :heavy_check_mark: | :x: | :x: | :x: |
| 2016  | :heavy_check_mark: | :x: | :x: | :x: |
| 2015  | :heavy_check_mark: | :x: | :x: | :x: |
| 2014  | :heavy_check_mark: | :x: | :x: |  -- |
| 2013  | :heavy_check_mark: |  -- |  -- |  -- |
| 2012  | :heavy_check_mark: |  -- |  -- |  -- |
| 2011  | :heavy_check_mark: |  -- |  -- |  -- |


## Available scripts

| Germany | France | Great Britain | Nordic Grid |
|:---:|:---:|:---:|:---:|
| :heavy_check_mark: | :x: | :x: | :x: |


# Changelog
- Version 0.3 - Moving to Github to produce a long-term repository.
- Version 0.2 - Moved to [JuGit](https://jugit.fz-juelich.de/) server
- Version 0.1 - Initial construction based files on a [Sciebo](https://www.sciebo.de/) folder

# Contributions
If you have open data from power-grid system, be it frequency, voltages, load, consumption, models, we will welcome all contributions to enhance this database

## Affiliated institutions and collaborators

This project came to life by Leonardo Rydin Gorjão in 2018 on a GitHub repository.

### Funding
Helmholtz Association Initiative *Energy System 2050 - A Contribution of the Research Field Energy* and the grant No. VH-NG-1025.
