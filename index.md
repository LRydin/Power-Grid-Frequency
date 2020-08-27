---
Title: Home

menus:
  main:
    weight: 1
    title: Home
layout: splash
classes: wide
---


<div id="map" class="leafmap"></div>

<script type="text/javascript" src="assets/GeoJSON/WesternInterconnection.js"></script>
<script type="text/javascript" src="assets/GeoJSON/TexasInterconnection.js"></script>
<script type="text/javascript" src="assets/GeoJSON/NordicGrid.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Russian.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Baltic.js"></script>
<script type="text/javascript" src="assets/GeoJSON/NationalGrid.js"></script>
<script type="text/javascript" src="assets/GeoJSON/ContinentalEurope.js"></script>
<!--
	<script type="text/javascript" src="assets/GeoJSON/Irish.js"></script>
-->
<script type="text/javascript" src="assets/GeoJSON/Iceland.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Faroe.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Mallorca.js"></script>
<script type="text/javascript" src="assets/GeoJSON/GranCanaria.js"></script>
<script type="text/javascript" src="assets/GeoJSON/SouthAfrica.js"></script>

<script>

var viirs = 'VIIRS_SNPP_CorrectedReflectance_TrueColor';

var basemap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    'attribution': '&copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Made with <a href="https://www.naturalearthdata.com/">Natural Earth</a>',
    'minZoom': 2,
    'maxZoom': 19
  });



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


var greenpurpleIcon = L.icon({
    iconUrl: 'assets/js/images/marker-icon-green-purple.png',
    shadowUrl: 'assets/js/images/marker-shadow.png',
		iconSize:    [25, 41],
		iconAnchor:  [12, 41],
		popupAnchor: [1, -34],
		tooltipAnchor: [16, -28],
		shadowSize:  [41, 41]
});

var greenblueIcon = L.icon({
    iconUrl: 'assets/js/images/marker-icon-green-blue.png',
    shadowUrl: 'assets/js/images/marker-shadow.png',
		iconSize:    [25, 41],
		iconAnchor:  [12, 41],
		popupAnchor: [1, -34],
		tooltipAnchor: [16, -28],
		shadowSize:  [41, 41]
});

var yellowIcon = L.icon({
    iconUrl: 'assets/js/images/marker-icon-yellow.png',
    shadowUrl: 'assets/js/images/marker-shadow.png',
		iconSize:    [25, 41],
		iconAnchor:  [12, 41],
		popupAnchor: [1, -34],
		tooltipAnchor: [16, -28],
		shadowSize:  [41, 41]
});

var TransnetBW      = L.marker([ 48.777111, 9.180770]),
    RTE             = L.marker([ 48.856666, 2.3522]),
		FinGrid         = L.marker([ 60.169857, 24.938379]);

var Cork     	      = L.marker([ 51.8, -8.4 ], {icon: greenIcon}),
    Reykjavik     	= L.marker([ 64.1, -21.7], {icon: greenIcon}),
    Vestmanna     	= L.marker([ 62.1, -7.1 ], {icon: greenIcon}),
    GranCanaria     = L.marker([ 28.1, -15.4], {icon: greenIcon}),
    PalmaMallorca 	= L.marker([ 39.5,  2.6 ], {icon: greenIcon}),
    London        	= L.marker([ 51.5, -0.00], {icon: greenblueIcon}),
    Lauris        	= L.marker([ 43.746460,  5.313320], {icon: greenIcon}),
		Split         	= L.marker([ 43.508133,  16.440193], {icon: greenIcon}),
		Erice         	= L.marker([ 38.036740,  12.583740], {icon: greenIcon}),
		Krakau        	= L.marker([ 51.205551,  16.211000], {icon: greenIcon}),
    Tallinn       	= L.marker([ 59.4,  24.7], {icon: greenIcon}),
    Stockholm     	= L.marker([ 59.3,  18.1], {icon: greenIcon}),
    SaltLake        = L.marker([ 40.6,-111.8], {icon: greenIcon}),
    College        	= L.marker([ 30.5, -96.3], {icon: greenIcon}),
    CapeTown        = L.marker([-33.9,  18.5], {icon: greenIcon}),
    StPetersburg    = L.marker([ 59.8,  30.3], {icon: greenIcon});


var	Karlsruhe     	= L.marker([ 49.0,  8.4 ], {icon: purpleIcon}),
    Oldenburg     	= L.marker([ 53.1,  8.2 ], {icon: purpleIcon}),
    Lisbon        	= L.marker([ 38.7, -9.1 ], {icon: greenpurpleIcon}),
    Istanbul      	= L.marker([ 41.0,  28.9], {icon: purpleIcon});

var Bekescsaba     	= L.marker([ 46.6,  21.0], {icon: yellowIcon}),
		Gyor          	= L.marker([ 47.6,  17.6], {icon: yellowIcon}),
		Zealand        	= L.marker([ 55.676098,  12.568337], {icon: yellowIcon});

// Cork.bindPopup('<b>Cork</b>, IE')
Reykjavik.bindPopup('<b>Reykjavik</b>, Iceland | Icelandic Grid</br> 2017-10-14 - 2017-10-20 | 5.6 days</br>  <a href="https://osf.io/sxph8/download">download</a> - 15.4 mb' )
Vestmanna.bindPopup('<b>Vestmanna</b>, Faroe Islands | Faroe Grid</br> 2019-11-03 - 2019-11-10 | 6.5 days</br> <a href="https://osf.io/a7h5b/download">download</a> - 24.5 mb')
GranCanaria.bindPopup('<b>Las Palmas de Gran Canaria</b>, Spain | Gran Canarian Grid</br> 2018-02-04 - 2018-02-10 | 6.5 days</br> <a href="https://osf.io/wz42b/download">download</a> - 16.2 mb<hr/> 2018-11-25 - 2018-11-26 | 1.5 days </br> <a href="https://osf.io/rukat/download">download</a> - 4.4 mb')
PalmaMallorca.bindPopup('<b>Palma de Mallorca</b>, Spain | Mallorcan Grid</br> 2019-09-29 - 2019-12-31 | 94.0 days </br> <a href="https://osf.io/2qn9k/download">download</a> - 324 mb')
London.bindPopup('<b>London</b>, United Kingdom | National Grid</br> 2019-03-04 - 2019-03-07 | 3.5 days </br> <a href="https://osf.io/cfv47/download">download</a> - 9.2 mb<hr/> 2019-11-10 - 2019-12-31 | 51.1 days </br> <a href="https://osf.io/h5ydu/download">download</a> - 135 mb<hr/>From January 2014 - December 2019</br> <a href="database/#great-britain">link to database</a> - 702.8 mb - 1 sec resolution')
Lauris.bindPopup('<b>Lauris</b>, France | Continental Europe</br> 2019-04-16 - 2019-04-27 | 12.0 days</br> <a href="https://osf.io/hfsrz/download">download</a> - 41.2 mb')
Split.bindPopup('<b>Split</b>, Croatia | Continental Europe</br> 2019-04-09 - 2019-04-12 | 4.0 days</br> <a href="https://osf.io/r9eh6/download">download</a> - 13.5 mb')
Erice.bindPopup('<b>Erice</b>, Italy | Continental Europe</br> 2019-07-02 - 2019-07-06 | 5.0 days</br> <a href="https://osf.io/c754b/download">download</a> - 17.1 mb')
Krakau.bindPopup('<b>Krakau</b>, Poland | Continental Europe</br> 2019-04-04 - 2019-04-07 | 4.0 days</br> <a href="https://osf.io/wq3te/download">download</a> - 13.6 mb')
Tallinn.bindPopup('<b>Tallinn</b>, Estonia | Baltic Grid</br> 2019-03-25 - 2019-04-17 | 22.9 days</br> <a href="https://osf.io/t5ske/download">download</a> - 79.0 mb')
Stockholm.bindPopup('<b>Stockholm</b>, Sweden | Nordic Grid</br> 2019-05-06 - 2019-05-13 | 6.7 days</br> <a href="https://osf.io/e2xfb/download">download</a> - 23.1 mb')
SaltLake.bindPopup('<b>Salt Lake City</b>, USA | Western Interconnection</br> 2019-05-19 - 2019-05-25 | 6.4 days</br> <a href="https://osf.io/8rp4v/download">download</a> - 16.5 mb')
College.bindPopup('<b>College Station</b>, USA | Texas Interconnection</br> 2019-05-15 - 2019-05-16 | 1.4 days</br> <a href="https://osf.io/t5wxz/download">download</a> - 3.7 mb<hr/>2019-05-20 - 2019-05-23 | 3.7 days</br> <a href="https://osf.io/zngy8/download">download</a> - 9.6 mb')
CapeTown.bindPopup('<b>Cape Town</b>, South Africa | South African Grid</br> 2017-11-19 - 2017-11-28 | 9.5 days</br> <a href="https://osf.io/gzk7d/download">download</a> - 27.0 mb')
StPetersburg.bindPopup('<b>St. Petersburg</b>, Russia | Russian Grid</br>2019-04-30 - 2019-05-12 | 13.0 days</br> <a href="https://osf.io/tvsyc/download">download</a> - 44.5 mb')

// Independent Measurements
Bekescsaba.bindPopup('<b>Békéscsaba</b>, Hungary | Continental Europe</br> 2019-07-09 - 2019-07-15 | 8 days</br> <a href="https://osf.io/pywx7/download">download</a> - 19.2 mb')
Gyor.bindPopup('<b>Győr</b>, Hungary | Continental Europe</br> 2019-07-09 - 2019-07-15 | 7 days</br> <a href="https://osf.io/u9ekr/download">download</a> - 18.8 mb</br> See data: Karlsruhe, Oldenburg, Lisbon, Istanbul')
Zealand.bindPopup('<b>Zealand</b>, Denmark | Nordic Grid</br> 2018-01-01 - 2018-12-31 | 365 days</br> <a href="database/#denmark">link to database</a> - 150.8 mb</br>')


// Sync Measurements
Karlsruhe.bindPopup('<b>Karlsruhe</b>, Germany | Continental Europe</br> 2019-07-09 - 2019-08-18 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 mb [4 locations synchronously]</br> See data: Békéscsaba, Győr, Hungary')
Oldenburg.bindPopup('<b>Oldenburg</b>, Germany | Continental Europe</br> 2019-07-10 - 2019-08-07 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 mb [4 locations synchronously]</br> See data: Békéscsaba, Győr, Hungary')
Lisbon.bindPopup('<b>Lisbon</b>, Portugal | Continental Europe</br> 2019-07-09 - 2019-08-18 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 mb [4 locations synchronously]</br> See data: Békéscsaba, Győr, Hungary<hr/> 2018-02-14 - 2018-02-21 | 6.8 days</br> <a href="https://osf.io/5zgwn/download">download</a> - 16.8 mb')
Istanbul.bindPopup('<b>Istanbul</b>, Turkey | Continental Europe</br> 2019-07-09 - 2019-08-16 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 mb [4 locations synchronously]</br> See data: Békéscsaba, Győr, Hungary')


// TSO data
TransnetBW.bindPopup('<b>Stuttgart</b>, Germany | Continental Europe</br> From July 2011 - March 2020</br> <a href="database/#continental-europe">link to database</a> - 1.1 gb - 1 sec resolution')
RTE.bindPopup('<b>Paris</b>, France | Continental Europe</br> From October 2014 - May 2020</br> <a href="database/#continental-europe">link to database</a> - 100.7 mb - 10 sec resolution')
FinGrid.bindPopup('<b>Helsinki</b>, Finland | Nordic Grid </br> From January 2015 - December 2019</br> <a href="database/#finland">link to database</a> - 5.1 gb - 0.1 sec resolution')


var SynchMeasurements = [
		[[49.0,  8.4],[53.1,  8.2]],
		[[49.0,  8.4],[38.7, -9.1]],
		[[49.0,  8.4],[41.0, 28.9]]
];

var SemiSynchMeasurements = [
    [[49.0,  8.4],[46.6,  21.0]],
		[[49.0,  8.4],[47.6,  17.6]]
];


var SynchMeasurementsLines = L.polyline(SynchMeasurements, {color: 'purple'})
var SemiSynchMeasurementsLines = L.polyline(SemiSynchMeasurements, {color: 'purple', dashArray: '6'})

var Europe = L.layerGroup([FinGrid, TransnetBW, RTE, Reykjavik, Vestmanna, GranCanaria, PalmaMallorca, Karlsruhe, Oldenburg, Lisbon, Istanbul, London, Lauris, Split, Erice, Krakau, Tallinn, Stockholm, Bekescsaba, Gyor, StPetersburg, Zealand, SynchMeasurementsLines, SemiSynchMeasurementsLines]);

var NorthAmerica = L.layerGroup([SaltLake, College]);

var Africa = L.layerGroup([CapeTown]);

// Deploy map

var map = L.map('map', {
  'center': [25, -5],
  'zoom': 2,
  'layers': [basemap, Europe, NorthAmerica, Africa]
});

// GeoJSONs

L.geoJson(WesternInterconnectionGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(TexasInterconnectionGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(NordicGridGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(RussianGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(BalticGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(NationalGridGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(ContinentalEuropeGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
// L.geoJson(IrishGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(IcelandGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(FaroeGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(MallorcaGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(GranCanariaGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(SouthAfricaGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);




// Layers and layer control

var LayerOfMap = { "<span style='color: black'><b>OpenStreetMap</b></span>": basemap };

var overlayMaps = {
    "<span style='color: black'>Europe</span>": Europe,
		"<span style='color: black'>North America</span>": NorthAmerica,
		"<span style='color: black'>Africa</span>": Africa
};

L.control.layers(LayerOfMap, overlayMaps).addTo(map);






// General properties


SynchMeasurementsLines.bindPopup("Synchronous Measurements between Karlsruhe, Oldenburg, Lisbon, and Istanbul. Békéscsaba and Győr, Hungary, also have recording, but not GPS synchronised.")

SemiSynchMeasurementsLines.bindPopup("Measurements in Békéscsaba and Győr, Hungary, in the same time frame as between Karlsruhe, Oldenburg, Lisbon, and Istanbul.")


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

function resetHighlight(e) { info.update(); }

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

    div.innerHTML = '<img id="x" src="assets/js/images/marker-icon-purple.png" width="20" height="20"/>' + '<h9>  Synchronous Measurements</h9></br>' +
		'<img id="x" src="assets/js/images/marker-icon-green.png" width="20" height="20"/>' + '<h9>  Standalone Measurements</h9></br>' +
		'<img id="x" src="assets/js/images/marker-icon.png" width="20" height="20"/>' + '<h9>  TSO Open Data Measurements</h9></br>'+
		'<img id="x" src="assets/js/images/marker-icon-yellow.png" width="20" height="20"/>' + '<h9>  Independent Measurements</h9>';

    return div;
};

legend.addTo(map);
info.addTo(map);

</script>


{% include_relative details.md %}
