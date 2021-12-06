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
<script type="text/javascript" src="assets/GeoJSON/Irish.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Iceland.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Faroe.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Mallorca.js"></script>
<script type="text/javascript" src="assets/GeoJSON/GranCanaria.js"></script>
<script type="text/javascript" src="assets/GeoJSON/SouthAfrica.js"></script>
<script type="text/javascript" src="assets/GeoJSON/Japan.js"></script>

<script>

// var viirs = 'VIIRS_SNPP_CorrectedReflectance_TrueColor';

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

var bluepurpleIcon = L.icon({
    iconUrl: 'assets/js/images/marker-icon-blue-purple.png',
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

var yellowTarget = L.icon({
    iconUrl: 'assets/js/images/marker-target-yellow.png',
    shadowUrl: 'assets/js/images/marker-target-shadow.png',
		iconSize:    [25, 25],
		iconAnchor:  [12, 12],
		popupAnchor: [1, -14],
		tooltipAnchor: [16, -28],
		shadowSize:  [27, 27]
});

var TransnetBW      = L.marker([ 48.777111, 9.180770], {time: "2013"}),
    RTE             = L.marker([ 48.856666, 2.3522], {time: "2014"}),
		FinGrid         = L.marker([ 60.186463, 24.829515], {icon: bluepurpleIcon, time: "2015"});

var Cork     	      = L.marker([ 51.8, -8.4 ], {icon: greenIcon, time: "2017"}),
    Reykjavik     	= L.marker([ 64.1, -21.7], {icon: greenIcon, time: "2017"}),
    Vestmanna     	= L.marker([ 62.1, -7.1 ], {icon: greenIcon, time: "2019"}),
    GranCanaria     = L.marker([ 28.1, -15.4], {icon: greenIcon, time: "2018"}),
    PalmaMallorca 	= L.marker([ 39.5,  2.6 ], {icon: greenIcon, time: "2019"}),
    London        	= L.marker([ 51.5, -0.00], {icon: greenblueIcon, time: "2015"}),
    Lauris        	= L.marker([ 43.746460,  5.313320], {icon: greenIcon, time: "2015"}),
		Split         	= L.marker([ 43.508133,  16.440193], {icon: greenIcon, time: "2015"}),
		Erice         	= L.marker([ 38.036740,  12.583740], {icon: greenIcon, time: "2015"}),
		Krakau        	= L.marker([ 51.205551,  16.211000], {icon: greenIcon, time: "2015"}),
    Tallinn       	= L.marker([ 59.4,  24.7], {icon: greenIcon, time: "2015"}),
    Stockholm     	= L.marker([ 59.350029, 18.070009], {icon: greenpurpleIcon, time: "2015"}),
    SaltLake        = L.marker([ 40.6,-111.8], {icon: greenIcon, time: "2015"}),
    College        	= L.marker([ 30.5, -96.3], {icon: greenIcon, time: "2015"}),
    CapeTown        = L.marker([-33.9,  18.5], {icon: greenIcon, time: "2015"}),
    StPetersburg    = L.marker([ 59.8,  30.3], {icon: greenIcon, time: "2015"});


var	Karlsruhe     	= L.marker([ 49.0,  8.4 ], {icon: purpleIcon}),
    Oldenburg     	= L.marker([ 53.1,  8.2 ], {icon: purpleIcon}),
    Lisbon        	= L.marker([ 38.7, -9.1 ], {icon: greenpurpleIcon}),
    Istanbul      	= L.marker([ 41.0,  28.9], {icon: purpleIcon});

var Bekescsaba     	= L.marker([ 46.6,  21.0], {icon: yellowIcon}),
		Gyor          	= L.marker([ 47.6,  17.6], {icon: yellowIcon}),
		DTU1          	= L.marker([ 55.693589, 12.097191], {icon: yellowIcon}),
		DTU2          	= L.marker([ 56.162937, 10.203921], {icon: yellowIcon}),
    Tokyo           = L.marker([ 35.682604,139.752766], {icon: yellowIcon}),
    NorthSweden     = L.marker([ 66.353562, 19.323426], {icon: yellowTarget}),
    MidSweden       = L.marker([ 63.126178, 15.205319], {icon: yellowTarget}),
    SouthSweden     = L.marker([ 58.310608, 14.511484], {icon: yellowTarget}),
    Dublin     	    = L.marker([ 53.306656, -6.225348], {icon: yellowIcon});

var STRONg2rid_CTH  = L.marker([ 57.689769, 11.973701], {icon: purpleIcon}),
    STRONg2rid_LTH  = L.marker([ 55.711850, 13.210120], {icon: purpleIcon}),
    STRONg2rid_LTU  = L.marker([ 65.617792, 22.135986], {icon: purpleIcon}),
    STRONg2rid_TTY  = L.marker([ 61.494200, 23.780750], {icon: purpleIcon}),
    STRONg2rid_NTNU = L.marker([ 63.419443, 10.401995], {icon: purpleIcon});


var KIT_logo = '<img src="assets/img/KIT_logo.jpg" width="45" height="45"/></br>'
var DTU_logo = '<img src="assets/img/DTU_logo.jpg" width="25" height="35"/></br>'
var NG_logo = '<img src="assets/img/NG_logo.jpg" width="100" height="35"/></br>'
var RTE_logo = '<img src="assets/img/RTE_logo.jpg" width="35" height="35"/></br>'
var TransNetBW_logo = '<img src="assets/img/TransNetBW_logo.jpg" width="100" height="35"/></br>'
var Fingrid_logo = '<img src="assets/img/Fingrid_logo.jpg" width="100" height="35"/></br>'
var MAVIR_logo = '<img src="assets/img/MAVIR_logo.jpg" width="45" height="35"/></br>'


// Cork.bindPopup('<b>Cork</b>, IE')
Reykjavik.bindPopup(KIT_logo + '<b>Reykjavik</b>, Iceland | Icelandic Grid</br> 2017-10-14 - 2017-10-20 | 5.6 days</br>  <a href="https://osf.io/sxph8/download">download</a> - 15.4 MB', {maxWidth:500})
Vestmanna.bindPopup(KIT_logo + '<b>Vestmanna</b>, Faroe Islands | Faroe Grid</br> 2019-11-03 - 2019-11-10 | 6.5 days</br> <a href="https://osf.io/a7h5b/download">download</a> - 24.5 MB', {maxWidth:500})
GranCanaria.bindPopup(KIT_logo + '<b>Las Palmas de Gran Canaria</b>, Spain | Gran Canarian Grid</br> 2018-02-04 - 2018-02-10 | 6.5 days</br> <a href="https://osf.io/wz42b/download">download</a> - 16.2 MB<hr/> 2018-11-25 - 2018-11-26 | 1.5 days </br> <a href="https://osf.io/rukat/download">download</a> - 4.4 MB', {maxWidth:500})
PalmaMallorca.bindPopup(KIT_logo + '<b>Palma de Mallorca</b>, Spain | Mallorcan Grid</br> 2019-09-29 - 2019-12-31 | 94.0 days </br> <a href="https://osf.io/2qn9k/download">download</a> - 324 MB', {maxWidth:500})
London.bindPopup(KIT_logo + '<b>London</b>, United Kingdom | National Grid</br> 2019-03-04 - 2019-03-07 | 3.5 days </br> <a href="https://osf.io/cfv47/download">download</a> - 9.2 MB<hr/> 2019-11-10 - 2019-12-31 | 51.1 days </br> <a href="https://osf.io/h5ydu/download">download</a> - 135 MB<hr/>' + NG_logo + 'From January 2014 - December 2019</br> <a href="database/#great-britain">link to database</a> - 702.8 MB - 1 sec resolution', {maxWidth:500})
Lauris.bindPopup(KIT_logo + '<b>Lauris</b>, France | Continental Europe</br> 2019-04-16 - 2019-04-27 | 12.0 days</br> <a href="https://osf.io/hfsrz/download">download</a> - 41.2 MB', {maxWidth:500})
Split.bindPopup(KIT_logo + '<b>Split</b>, Croatia | Continental Europe</br> 2019-04-09 - 2019-04-12 | 4.0 days</br> <a href="https://osf.io/r9eh6/download">download</a> - 13.5 MB', {maxWidth:500})
Erice.bindPopup(KIT_logo + '<b>Erice</b>, Italy | Continental Europe</br> 2019-07-02 - 2019-07-06 | 5.0 days</br> <a href="https://osf.io/c754b/download">download</a> - 17.1 MB', {maxWidth:500})
Krakau.bindPopup(KIT_logo + '<b>Krakau</b>, Poland | Continental Europe</br> 2019-04-04 - 2019-04-07 | 4.0 days</br> <a href="https://osf.io/wq3te/download">download</a> - 13.6 MB', {maxWidth:500})
Tallinn.bindPopup(KIT_logo + '<b>Tallinn</b>, Estonia | Baltic Grid</br> 2019-03-25 - 2019-04-17 | 22.9 days</br> <a href="https://osf.io/t5ske/download">download</a> - 79.0 MB', {maxWidth:500})


Stockholm.bindPopup(KIT_logo + '<b>Stockholm</b>, Sweden | Nordic Grid</br> 2019-05-06 - 2019-05-13 | 6.7 days</br> <a href="https://osf.io/e2xfb/download">download</a> - 23.1 MB <hr/> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/wmuct/download">download</a> - 20.5 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})


SaltLake.bindPopup(KIT_logo + '<b>Salt Lake City</b>, USA | Western Interconnection</br> 2019-05-19 - 2019-05-25 | 6.4 days</br> <a href="https://osf.io/8rp4v/download">download</a> - 16.5 MB', {maxWidth:500})
College.bindPopup(KIT_logo + '<b>College Station</b>, USA | Texas Interconnection</br> 2019-05-15 - 2019-05-16 | 1.4 days</br> <a href="https://osf.io/t5wxz/download">download</a> - 3.7 MB<hr/>2019-05-20 - 2019-05-23 | 3.7 days</br> <a href="https://osf.io/zngy8/download">download</a> - 9.6 MB', {maxWidth:500})
CapeTown.bindPopup(KIT_logo + '<b>Cape Town</b>, South Africa | South African Grid</br> 2017-11-19 - 2017-11-28 | 9.5 days</br> <a href="https://osf.io/gzk7d/download">download</a> - 27.0 MB', {maxWidth:500})
StPetersburg.bindPopup(KIT_logo + '<b>St. Petersburg</b>, Russia | Russian Grid</br>2019-04-30 - 2019-05-12 | 13.0 days</br> <a href="https://osf.io/tvsyc/download">download</a> - 44.5 MB', {maxWidth:500})

// Independent Measurements
Bekescsaba.bindPopup(MAVIR_logo + '<b>Békéscsaba</b>, Hungary | Continental Europe</br> 2019-07-09 - 2019-07-15 | 8 days</br> <a href="https://osf.io/pywx7/download">download</a> - 19.2 MB</br> See data: Karlsruhe, Oldenburg, Lisbon, Istanbul', {maxWidth:500})
Gyor.bindPopup(MAVIR_logo + '<b>Győr</b>, Hungary | Continental Europe</br> 2019-07-09 - 2019-07-15 | 7 days</br> <a href="https://osf.io/u9ekr/download">download</a> - 18.8 MB</br> See data: Karlsruhe, Oldenburg, Lisbon, Istanbul', {maxWidth:500})
DTU1.bindPopup(DTU_logo + '<b>Zealand</b>, Denmark | Nordic Grid</br> 2018-01-01 - 2018-12-31 | 365 days</br> <a href="database/#denmark-1">link to database</a> - 150.8 MB</br> <hr/> 2019-01-01 - 2019-12-31 | 365 days</br> <a href="database/#denmark-1">link to database</a> - 298.1 MB</br>', {maxWidth:500})
DTU2.bindPopup(DTU_logo + '<b>Central Jutland</b>, Denmark | Continental Europe</br> 2019-01-01 - 2019-12-31 | 365 days</br> <a href="database/#denmark">link to database</a> - 286.1 MB</br>', {maxWidth:500})
Tokyo.bindPopup(DTU_logo + '<b>Tokyo</b>, Japan | Japanese 50Hz</br> 20220-01-01 - 2020-12-31 | 317 days</br> <a href="database/#japan">link to database</a> - 250.3 MB</br>', {maxWidth:500})
NorthSweden.bindPopup('<b>North Sweden</b>, Sweden | Nordic Grid</br> 2020-01-01 - 2020-12-31 | 366 days</br> <a href="database/#sweden">link to database</a> - 9.0 GB</br>', {maxWidth:500})
MidSweden.bindPopup('<b>Mid Sweden</b>, Sweden | Nordic Grid</br> 2020-01-01 - 2020-12-31 | 366 days</br> <a href="database/#sweden">link to database</a> - 9.2 GB</br>', {maxWidth:500})
SouthSweden.bindPopup('<b>South Sweden</b>, Sweden | Nordic Grid</br> 2020-01-01 - 2020-12-31 | 366 days</br> <a href="database/#sweden">link to database</a> - 9.1 GB</br>', {maxWidth:500})
Dublin.bindPopup('<b>Dublin</b>, Ireland | EirGrid</br> 2014  <a href="https://osf.io/y9nrh/download">download</a> - 1.22 GB<hr/>2015  <a href="https://osf.io/38fnx/download">download</a> - 2.56 GB<hr/>2016  <a href="https://osf.io/8dqk2/download">download</a> - 1.79 GB<hr/>2017  <a href="https://osf.io/5rsq9/download">download</a> - 2.35 GB', {maxWidth:500})

// Sync Measurements
Karlsruhe.bindPopup(KIT_logo + '<b>Karlsruhe</b>, Germany | Continental Europe</br> 2019-07-09 - 2019-08-18 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 MB [4 locations synchronously]</br> See data: Békéscsaba and Győr, Hungary', {maxWidth:500})
Oldenburg.bindPopup(KIT_logo + '<b>Oldenburg</b>, Germany | Continental Europe</br> 2019-07-10 - 2019-08-07 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 MB [4 locations synchronously]</br> See data: Békéscsaba and Győr, Hungary', {maxWidth:500})
Lisbon.bindPopup(KIT_logo + '<b>Lisbon</b>, Portugal | Continental Europe</br> 2019-07-09 - 2019-08-18 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 MB [4 locations synchronously]</br> See data: Békéscsaba and Győr, Hungary<hr/> 2018-02-14 - 2018-02-21 | 6.8 days</br> <a href="https://osf.io/5zgwn/download">download</a> - 16.8 MB', {maxWidth:500})
Istanbul.bindPopup(KIT_logo + '<b>Istanbul</b>, Turkey | Continental Europe</br> 2019-07-09 - 2019-08-16 | 41.0 days</br> <a href="https://osf.io/p5xyr/download">download</a> - 218 MB [4 locations synchronously]</br> See data: Békéscsaba and Győr, Hungary', {maxWidth:500})

STRONg2rid_CTH.bindPopup('<b>Gothenburg</b>, Sweden | Nordic Grid</br> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/prqk8/download">download</a> - 20.6 MB | [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})
STRONg2rid_LTH.bindPopup('<b>Lund</b>, Sweden | Nordic Grid</br> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/8sp9k/download">download</a> - 22.4 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})
// STRONg2rid_KTH.bindPopup('<b>Stockholm</b>, Sweden | Nordic Grid</br> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/wmuct/download">download</a> - 20.5 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})
STRONg2rid_LTU.bindPopup('<b>Luleå</b>, Sweden | Nordic Grid</br> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/ar4jn/download">download</a> - 22.0 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})
STRONg2rid_TTY.bindPopup('<b>Tampere</b>, Finland | Nordic Grid</br> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/nfu5d/download">download</a> - 20.0 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})
// STRONg2rid_AU.bindPopup('<b>Aalto</b>, Finland | Nordic Grid</br> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/qb3sa/download">download</a> - 27.3 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})
STRONg2rid_NTNU.bindPopup('<b>Trondheim</b>, Norway | Nordic Grid</br> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/67fjs/download">download</a> - 28.3 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})

// TSO data
TransnetBW.bindPopup(TransNetBW_logo + '<b>Stuttgart</b>, Germany | Continental Europe</br> From July 2011 - March 2020</br> <a href="database/#continental-europe">link to database</a> - 1.1 GB - 1 sec resolution')
RTE.bindPopup(RTE_logo + '<b>Paris</b>, France | Continental Europe</br> From October 2014 - May 2020</br> <a href="database/#continental-europe">link to database</a> - 100.7 MB - 10 sec resolution')

FinGrid.bindPopup(Fingrid_logo + '<b>Helsinki</b>, Finland | Nordic Grid </br> From January 2015 - December 2019</br> <a href="database/#finland">link to database</a> - 5.1 GB - 0.1 sec resolution <hr/> 2013-09-09 - 2013-09-11 | 1.5 days </br> <a href="https://osf.io/wmuct/download">download</a> - 20.5 MB [7 locations synchronously]</br> <a href="database/#synchronised-measurements">link to database</a>', {maxWidth:500})


var SynchMeasurements = [
		[[49.0,  8.4],[53.1,  8.2]],
		[[49.0,  8.4],[38.7, -9.1]],
		[[49.0,  8.4],[41.0, 28.9]]
];

var SemiSynchMeasurements = [
    [[49.0,  8.4],[46.6,  21.0]],
		[[49.0,  8.4],[47.6,  17.6]]
];

var SemiSynchMeasurementsNG = [
    [[63.126178, 15.205319],[66.353562, 19.323426]],
		[[63.126178, 15.205319],[58.310608, 14.511484]]
];

var SemiSynchMeasurementsNGSTRONG = [
    [[59.350029, 18.070009],[57.689769, 11.973701]],
    [[59.350029, 18.070009],[55.711850, 13.210120]],
    [[59.350029, 18.070009],[65.617792, 22.135986]],
    [[59.350029, 18.070009],[61.494200, 23.780750]],
    [[59.350029, 18.070009],[60.186463, 24.829515]],
    [[59.350029, 18.070009],[63.419443, 10.401995]]
];

var SynchMeasurementsLines = L.polyline(SynchMeasurements, {color: 'purple'})
var SemiSynchMeasurementsLines = L.polyline(SemiSynchMeasurements, {color: 'purple', dashArray: '6'})
var SemiSynchMeasurementsNGLines = L.polyline(SemiSynchMeasurementsNG, {color: 'gold', dashArray: '6'})
var SemiSynchMeasurementsNGSTRONGLines = L.polyline(SemiSynchMeasurementsNGSTRONG, {color: 'purple', dashArray: '6'})

var Europe = L.layerGroup([FinGrid, TransnetBW, RTE, Reykjavik, Vestmanna, GranCanaria, PalmaMallorca, Karlsruhe, Oldenburg, Lisbon, Istanbul, London, Lauris, Split, Erice, Krakau, Tallinn, Stockholm, Bekescsaba, Gyor, StPetersburg, DTU1, DTU2, NorthSweden, MidSweden, SouthSweden, SynchMeasurementsLines, SemiSynchMeasurementsLines, SemiSynchMeasurementsNGLines, SemiSynchMeasurementsNGSTRONGLines, Dublin]);

var NorthAmerica = L.layerGroup([SaltLake, College]);

var Asia = L.layerGroup([Tokyo]);

var Africa = L.layerGroup([CapeTown]);


// Sectioning years
var TSOs = L.layerGroup([TransnetBW, RTE, FinGrid, London]);
var y2020 = L.layerGroup([Tokyo, NorthSweden, MidSweden, SouthSweden, SemiSynchMeasurementsNGLines]);
var y2019 = L.layerGroup([Vestmanna, GranCanaria, Karlsruhe, Oldenburg, Lisbon, Istanbul, Lauris, Split, Erice, Krakau, Tallinn, Stockholm, Bekescsaba, Gyor, StPetersburg, SaltLake, College, SynchMeasurementsLines, SemiSynchMeasurementsLines]);
var y2018 = L.layerGroup([PalmaMallorca, DTU1, DTU2]);
var y2017 = L.layerGroup([TransnetBW, Reykjavik, CapeTown, Dublin]);
var y2016 = L.layerGroup([TransnetBW, Dublin]);
var y2015 = L.layerGroup([TransnetBW, Dublin]);
var y2014 = L.layerGroup([TransnetBW, Dublin]);
var y2013 = L.layerGroup([STRONg2rid_CTH, STRONg2rid_LTH, Stockholm, STRONg2rid_LTU, STRONg2rid_TTY, FinGrid, STRONg2rid_NTNU, SemiSynchMeasurementsNGSTRONGLines]);
var y2012 = L.layerGroup([TransnetBW]);
var y2011 = L.layerGroup([TransnetBW]);

// Deploy  

var map = L.map('map', {
  'center': [25, -5],
  'zoom': 2,
  'layers': [basemap, y2020, y2019, y2018, y2017, y2016, y2015, y2014, y2013, y2012, y2011]
});

// GeoJSONs

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
L.geoJson(SouthAfricaGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);
L.geoJson(JapanGeo, {style: style, onEachFeature: onEachFeature}).addTo(map);


// Layers and layer control

var LayerOfMap = { "<span style='color: black'><b>OpenStreetMap</b></span>": basemap};

var overlayMaps = {
    "<span style='color: black'>2020</span>": y2020,
    "<span style='color: black'>2019</span>": y2019,
    "<span style='color: black'>2018</span>": y2018,
    "<span style='color: black'>2017</span>": y2017,
    "<span style='color: black'>2016</span>": y2016,
    "<span style='color: black'>2015</span>": y2015,
    "<span style='color: black'>2014</span>": y2014,
    "<span style='color: black'>2013</span>": y2013,
    "<span style='color: black'>2012</span>": y2012,
    "<span style='color: black'>2011</span>": y2011,
};

L.control.layers(LayerOfMap, overlayMaps).addTo(map);

// General properties

SynchMeasurementsLines.bindPopup("GPS-Synchronous recordings from Karlsruhe, Oldenburg, Lisbon, and Istanbul. Also: Békéscsaba and Győr, Hungary, yet not GPS synchronised.")
SemiSynchMeasurementsLines.bindPopup("Measurements in Békéscsaba and Győr, Hungary, in the same time frame as between Karlsruhe, Oldenburg, Lisbon, and Istanbul.")
SemiSynchMeasurementsNGLines.bindPopup("Measurements in the north, middle, and south of Sweden. Locations are indicative, due to data protection.")
SemiSynchMeasurementsNGSTRONGLines.bindPopup("Synchronous recordings from Gothenburg, Lund, Stockholm, and Luleå, Sweden, Tampere and Aalto, Finland, and Trondheim, Norway")


SynchMeasurementsLines.bringToFront()
SemiSynchMeasurementsLines.bringToFront()
SemiSynchMeasurementsNGLines.bringToFront()
SemiSynchMeasurementsNGSTRONGLines.bringToFront()

// SynchMeasurementsLines.on('mouseover', function (e) { this.openPopup(); });
// SynchMeasurementsLines.on('mouseout', function (e) { this.closePopup(); });

// SemiSynchMeasurementsLines.on('mouseover', function (e) { this.openPopup(); });
// SemiSynchMeasurementsLines.on('mouseout', function (e) { this.closePopup(); });

// SemiSynchMeasurementsNGLines.on('mouseover', function (e) { this.openPopup(); });
// SemiSynchMeasurementsNGLines.on('mouseout', function (e) { this.closePopup(); });

// SemiSynchMeasurementsNGSTRONGLines.on('mouseover', function (e) { this.openPopup(); });
// SemiSynchMeasurementsNGSTRONGLines.on('mouseout', function (e) { this.closePopup(); });


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
		'<img id="x" src="assets/js/images/marker-icon-yellow.png" width="20" height="20"/>' + '/' + '<img id="x" src="assets/js/images/marker-target-yellow.png" width="30" height="30"/>' + '<h9>  Independent Measurements</h9>';

    return div;
};

legend.addTo(map);
info.addTo(map);


// layerGroup = L.layerGroup([TransnetBW, RTE, FinGrid, Reykjavik, Vestmanna, GranCanaria, PalmaMallorca]);
// var slider = L.control.sliderControl({
//     layer: layerGroup,
//     position: "bottomright",
//     range: true
// });

// alwaysShowDate: true,
// timeStrLength: 4,
// range: true,
// orderMarkers: true,
// showAllOnStart: true,
// showPopups: false


// map.addControl(slider);
// slider.startSlider();
// slider.on('rangechanged',function (e) {
//     console.log(e)
// });

</script>

{% include_relative details.md %}
