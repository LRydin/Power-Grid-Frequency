---
Title: Home

latlng: [42.41, 2.22]
zoom: 5
mlatlng: [52.11, 12.44]
icon: _sass/js/images/marker-icon-2x.png
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
// L.Icon.Default.imagePath = '{{ "images/carto/" | prepend: site.baseurl }}';

var viirs = 'VIIRS_SNPP_CorrectedReflectance_TrueColor';
// var modis = 'MODIS_Terra_CorrectedReflectance_TrueColor';

var basemap = {
  'OpenStreetMap': L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    'attribution': '&copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors',
    'minZoom': 2,
    'maxZoom': 19
  }),
  'Thunderforest': L.tileLayer('https://{s}.tile.thunderforest.com/' + '{% if include.tf_layer %}{{ include.tf_layer }}{% else %}outdoors{% endif %}' + '/{z}/{x}/{y}.png', {
    'attribution': 'Maps &copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors',
    'minZoom': 2,
    'maxZoom': 19
  }),
  'Carto': L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/' + '{% if include.c_layer %}{{ include.c_layer }}{% else %}dark_all{% endif %}' + '/{z}/{x}/{y}.png', {
    'attribution': '&copy; <a href="http://cartodb.com/attributions">CartoDB</a>, &copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors',
    'minZoom': 2,
    'maxZoom': 19
  }),
  'Esri': L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    'attribution': 'Tiles &copy; Esri, &copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors',
    'minZoom': 3,
    'maxZoom': 18
  }),
  'Gibs': L.tileLayer('https://map1.vis.earthdata.nasa.gov/wmts-webmerc/' + viirs + '/default/' + '{{ page.date| date: "%Y-%m-%d" }}' + '/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg', {
    'attribution': 'Maps &copy; <a href="http://earthdata.nasa.gov">Gibs</a>, &copy; <a href="https://osmlab.github.io/attribution-mark/copyright/?name={{ site.title }}">OpenStreetMap</a> contributors',
    'minZoom': 3,
    'maxZoom': 9
  })
};

var map = L.map('map', {
  {% if page.latlng %}
  'center': [{{ page.latlng[0] }}, {{ page.latlng[1] }}],
  'zoom': {{ page.zoom }},
  {% if include.leaflet_tile %}
  'layers': [basemap.{{ include.leaflet_tile }}]
  {% else %}
  'layers': [basemap.OpenStreetMap]
  {% endif %}
	{% endif %}
});


{% for i in (0..17) %}
var marker = L.marker(
  [{{ page.lon[i] }}, {{ page.lat[i] }}]
).addTo(map);
marker.bindPopup("{{ page.locations[i] }}").openPopup();
{% endfor %}


</script>


{% include_relative details.md %}
