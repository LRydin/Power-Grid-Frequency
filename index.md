---
Title: Home

leaflet: True
latlng: [25, -15]
zoom: 2
mlatlng: [52.11, 12.44]
icon: assests/js/images/marker-icon.png
mpop: KIT

lon: [51.8,64.1,62.1,28.1,39.5,49.0,53.1,38.7 ,41.0 ,51.5 ,59.4 ,59.3,40.6,30.5,-33.9,59.8, 46.679, 47.6842]
lat: [ -8.4,-21.7,-7.1,-15.4, 2.6, 8.4,8.2,-9.1, 28.9,-0.0, 24.7, 18.1 , -111.8 ,-96.3 , 18.5 ,30.3, 21, 17.6344]
locations: ['Cork', 'Reykjavik', 'Vestmanna', 'Gran Canaria', 'Palma de Mallorca','Karlsruhe','Oldenburg','Lisbon', 'Istanbul', 'London', 'Tallinn', 'Stockholm', 'Salt Lake City', 'College Station', 'Cape Town', 'St Petersburg', 'Békéscsaba', 'Győr']


menus:
  main:
    weight: 1
    title: Home
layout: splash
classes: wide
---


<style type="text/css">
#map {
	width:100%;
	height:500px;
}
</style>

<div id="map" class="leafmap"></div>

<script>

var viirs = 'VIIRS_SNPP_CorrectedReflectance_TrueColor';

var basemap = {
  'OpenStreetMap': L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    'attribution': '&copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    'minZoom': 2,
    'maxZoom': 19
  })
};


var Cork     	      = L.marker([ 51.8, -8.4  ]).bindPopup('Cork'),
    Reykjavik     	= L.marker([ 64.1, -21.7 ]).bindPopup('Reykjavik'),
    Vestmanna     	= L.marker([ 62.1, -7.1  ]).bindPopup('Vestmanna'),
    GranCanaria     = L.marker([ 28.1, -15.4 ]).bindPopup('Gran Canaria'),
    PalmaMallorca 	= L.marker([ 39.5,  2.6  ]).bindPopup('Palma de Mallorca'),
    Karlsruhe     	= L.marker([ 49.0,  8.4  ]).bindPopup('Karlsruhe'),
    Oldenburg     	= L.marker([ 53.1,  8.2  ]).bindPopup('Oldenburg'),
    Lisbon        	= L.marker([ 38.7, -9.1  ]).bindPopup('Lisbon'),
    Istanbul      	= L.marker([ 41.0,  28.9 ]).bindPopup('Istanbul'),
    London        	= L.marker([ 51.5, -0.00 ]).bindPopup('London'),
    Tallinn       	= L.marker([ 59.4,  24.7 ]).bindPopup('Tallinn'),
    Stockholm     	= L.marker([ 59.3,  18.1 ]).bindPopup('Stockholm'),
    SaltLake        = L.marker([ 40.6,-111.8 ]).bindPopup('Salt Lake City'),
    College        	= L.marker([ 30.5, -96.3 ]).bindPopup('College Station'),
    CapeTown        = L.marker([-33.9,  18.5 ]).bindPopup('Cape Town'),
    StPetersburg    = L.marker([ 59.8,  30.3 ]).bindPopup('St Petersburg'),
    Bekescsaba     	= L.marker([ 46.6,  21.0 ]).bindPopup('Békéscsaba'),
    Gyor          	= L.marker([ 47.6,  17.6 ]).bindPopup('Győr');


var Europe = L.layerGroup([Cork, Reykjavik, Vestmanna, GranCanaria, PalmaMallorca, Karlsruhe, Oldenburg, Lisbon, Istanbul, London, Tallinn, Stockholm]);

var USA = L.layerGroup([SaltLake, College]);

var Africa = L.layerGroup([CapeTown]);


var overlayMaps = {
    "<span style='color: black'>Europe</span>": Europe,
		"<span style='color: black'>USA</span>": USA,
		"<span style='color: black'>Africa</span>": Africa
};


var map = L.map('map', {
  'center': [25, -5],
  'zoom': 2,
  'layers': [basemap.OpenStreetMap, Europe, USA, Africa]
});


L.control.layers(basemap, overlayMaps).addTo(map);

</script>


{% include_relative details.md %}
