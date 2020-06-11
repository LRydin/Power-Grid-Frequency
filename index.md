---
Title: Home

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
.info {
    padding: 6px 8px;
    font: 14px/16px Arial, Helvetica, sans-serif;
    background: white;
    background: rgba(255,255,255,0.8);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
}
.info2 {
    padding: 6px 8px;
    font: 14px/16px Arial, Helvetica, sans-serif;
    background: white;
    background: rgba(255,255,255,0.8);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
}
.info h9 {
    margin: 0 0 5px;
    color: #000000;
}
</style>

<div id="map" class="leafmap"></div>

<script type="text/javascript" src="assets/GeoJSON/WesternInterconnection.js"></script>
<script type="text/javascript" src="assets/GeoJSON/TexasInterconnection.js"></script>
<script type="text/javascript" src="assets/GeoJSON/NordicGrid.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Russian.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Baltic.js"></script>
<script type="text/javascript" src="assets/GeoJSON/NationalGrid.js"></script>
<script type="text/javascript" src="assets/GeoJSON/ContinentalEurope.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Irish.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Iceland.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Faroe.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Mallorca.js"></script>
<script type="text/javascript" src="assets/GeoJSON/GranCanaria.js"></script>


<script>

var viirs = 'VIIRS_SNPP_CorrectedReflectance_TrueColor';

var basemap = {
  'OpenStreetMap': L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    'attribution': '&copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Made with <a href="https://www.naturalearthdata.com/">Natural Earth</a>',
    'minZoom': 2,
    'maxZoom': 19
  })
};



var greenIcon = L.icon({
    iconUrl: 'assets/js/images/marker-icon-green.png',
    shadowUrl: 'assets/js/images/marker-shadow.png',
		iconSize:    [25, 41],
		iconAnchor:  [12, 41],
		popupAnchor: [1, -34],
		tooltipAnchor: [16, -28],
		shadowSize:  [41, 41]
});

var purpleIcon = L.icon({
    iconUrl: 'assets/js/images/marker-icon-purple.png',
    shadowUrl: 'assets/js/images/marker-shadow.png',
		iconSize:    [25, 41],
		iconAnchor:  [12, 41],
		popupAnchor: [1, -34],
		tooltipAnchor: [16, -28],
		shadowSize:  [41, 41]
});



var Cork     	      = L.marker([ 51.8, -8.4 ], {icon: greenIcon}).bindPopup('Cork'),
    Reykjavik     	= L.marker([ 64.1, -21.7], {icon: greenIcon}).bindPopup('Reykjavik'),
    Vestmanna     	= L.marker([ 62.1, -7.1 ], {icon: greenIcon}).bindPopup('Vestmanna'),
    GranCanaria     = L.marker([ 28.1, -15.4], {icon: greenIcon}).bindPopup('Gran Canaria'),
    PalmaMallorca 	= L.marker([ 39.5,  2.6 ], {icon: greenIcon}).bindPopup('Palma de Mallorca'),
    Karlsruhe     	= L.marker([ 49.0,  8.4 ], {icon: purpleIcon}).bindPopup('Karlsruhe'),
    Oldenburg     	= L.marker([ 53.1,  8.2 ], {icon: purpleIcon}).bindPopup('Oldenburg'),
    Lisbon        	= L.marker([ 38.7, -9.1 ], {icon: purpleIcon}).bindPopup('Lisbon'),
    Istanbul      	= L.marker([ 41.0,  28.9], {icon: purpleIcon}).bindPopup('Istanbul'),
    London        	= L.marker([ 51.5, -0.00], {icon: greenIcon}).bindPopup('London'),
    Tallinn       	= L.marker([ 59.4,  24.7], {icon: greenIcon}).bindPopup('Tallinn'),
    Stockholm     	= L.marker([ 59.3,  18.1], {icon: greenIcon}).bindPopup('Stockholm'),
    SaltLake        = L.marker([ 40.6,-111.8], {icon: greenIcon}).bindPopup('Salt Lake City'),
    College        	= L.marker([ 30.5, -96.3], {icon: greenIcon}).bindPopup('College Station'),
    CapeTown        = L.marker([-33.9,  18.5], {icon: greenIcon}).bindPopup('Cape Town'),
    StPetersburg    = L.marker([ 59.8,  30.3], {icon: greenIcon}).bindPopup('St Petersburg'),
    Bekescsaba     	= L.marker([ 46.6,  21.0], {icon: greenIcon}).bindPopup('Békéscsaba'),
    Gyor          	= L.marker([ 47.6,  17.6], {icon: greenIcon}).bindPopup('Győr');


var Europe = L.layerGroup([Cork, Reykjavik, Vestmanna, GranCanaria, PalmaMallorca, Karlsruhe, Oldenburg, Lisbon, Istanbul, London, Tallinn, Stockholm, Bekescsaba, Gyor, StPetersburg]);

var NorthAmerica = L.layerGroup([SaltLake, College]);

var Africa = L.layerGroup([CapeTown]);

var Synch = L.layerGroup([Karlsruhe, Oldenburg, Lisbon, Istanbul]);

var overlayMaps = {
    "<span style='color: black'>Europe</span>": Europe,
		"<span style='color: black'>North America</span>": NorthAmerica,
		"<span style='color: black'>Africa</span>": Africa
};


var map = L.map('map', {
  'center': [25, -5],
  'zoom': 2,
  'layers': [basemap.OpenStreetMap, Europe, NorthAmerica, Africa]
});


var SynchMeasurements = [
    [[49.0,  8.4],
		[53.1,  8.2]],
		[[49.0,  8.4],
		[38.7, -9.1]],
		[[49.0,  8.4],
		[41.0,  28.9]]
];

var SemiSynchMeasurements = [
    [[49.0,  8.4],
		[46.6,  21.0]],
		[[49.0,  8.4],
		[47.6,  17.6]]
];


var SynchMeasurementsLines = L.polyline(SynchMeasurements, {color: 'purple'}).addTo(map);
var SemiSynchMeasurementsLines = L.polyline(SemiSynchMeasurements, {color: 'purple', dashArray: '6'}).addTo(map);


SynchMeasurementsLines.bindPopup("Synchronous Measurements between Karlsruhe, Oldenburg, Lisbon, and Istanbul. Békéscsaba and Győr, Hungary, also have recording, but not GPS synchronised.")
SemiSynchMeasurementsLines.bindPopup("Measurements in Békéscsaba and Győr, Hungary, in the same time frame as between Karlsruhe, Oldenburg, Lisbon, and Istanbul.")


L.control.layers(basemap, overlayMaps).addTo(map);

// Power-grids

function style(feature) {
    return {
        fillColor: feature.colour,
        weight: 0,
        fillOpacity: 0.4
    };
}



var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

info.update = function (props) {
    this._div.innerHTML = '<h9>Synchronous Areas</h9><br />' +  (props ?
        '<b><h9>' + props.name + '</h9></b><br />'
        : '<h9>Hover over an area</h9>');
};

function highlightFeature(e) {
		var layer = e.target;
    info.update(layer.feature.properties);
}

function resetHighlight(e) {
    info.update();
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight
    });
}

var legend = L.control({position: 'bottomleft'});

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 10, 20, 50, 100, 200, 500, 1000],
        labels = [];

    div.innerHTML = '<img id="x" src="assets/js/images/marker-icon-purple.png" width="20" height="20"/>' + '<h9>  Synchronous Measurements </h9>';

    return div;
};

legend.addTo(map);


L.geoJson(WesternInterconnectionGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(TexasInterconnectionGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(NordicGridGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(RussianGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(BalticGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(NationalGridGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(ContinentalEuropeGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(IrishGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(IcelandGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(FaroeGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(MallorcaGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(GranCanariaGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);

info.addTo(map);






</script>


{% include_relative details.md %}
