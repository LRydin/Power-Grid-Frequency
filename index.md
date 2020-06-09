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
{% if page.leaflet %}
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
map.scrollWheelZoom.disable();
{% endif %}

{% if page.mlatlng %}
var marker = L.marker(
  [{{ page.mlatlng[0] }}, {{ page.mlatlng[1] }}]
).addTo(map);
{% endif %}

{% if page.icon %}
var xmarker = L.icon({
  iconUrl: '{{ page.icon | prepend: site.baseurl }}',
  iconRetinaUrl: '{{ page.icon | prepend: site.baseurl }}',
  iconSize: [37, 50],
  iconAnchor: [18.5, 50],
  popupAnchor: [0, -51]
});

var marker = L.marker([{{ page.mlatlng[0] }}, {{ page.mlatlng[1] }}], {
  icon: {{ page.icon }}
}).addTo(map);
{% endif %}

{% if page.mpop or page.icon %}
marker.bindPopup("{{ page.mpop }}").openPopup();
{% endif %}
</script>

{% include_relative details.md %}
