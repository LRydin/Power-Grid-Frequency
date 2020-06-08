---
Title: Home

leaflet: true
latlng: [42.42, 2.22]
zoom: 12
mlatlng: [42.11, 2.44]
icon: path/to/yourMarker.png
mpop: comment for your popup

menus:
  main:
    weight: 1
    title: Home
layout: single
---

## A Trial

This page presents an effort to bring power-grid frequency data from around the world, cleaned and processed for research usage.

The data is collected from the TSO's and is processed to remove dead recordings, spikes, and other naturally assumed bad measurements. The scripts that are used to clean the data are also available, for transparency. See the github page for sourcefiles.

The German data (1 sec recordings) are obtained from TransnetBW


var map = L.map('map', {
    center: [51.505, -0.09],
    zoom: 13
});
