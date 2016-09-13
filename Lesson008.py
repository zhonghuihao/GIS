from module_mesh import MeshCodeUtility
import folium
import geojson
from geojson import Polygon, MultiPolygon
from geojson import GeometryCollection
from geojson import Feature, FeatureCollection
import pandas as pd
import math
from urllib import request
from pygeocoder import Geocoder
import geocoder
import requests
import vincent
import gmplot
ENCODING = 'utf-8'
# Google_API Key: AIzaSyB4RT4NU_gZ6pNojdg1kQHaceSey1Z3WbY


# location = MeshCodeUtility.geocoding('qingdao')
# # (緯度,経度)
# lat = location['lat']
# lng = location['lng']
# print(MeshCodeUtility.get_1st_mesh(lat, lng))
# print(MeshCodeUtility.get_2nd_mesh(lat, lng))
# print(MeshCodeUtility.get_3rd_mesh(lat, lng))

# gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
# #
# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
# gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
# gmap.heatmap(heat_lats, heat_lngs)

# gmap.draw("mymap.html")

# import gmaps
# import gmaps.datasets
# gmaps.configure(api_key='AIzaSyB4RT4NU_gZ6pNojdg1kQHaceSey1Z3WbY')
# data = gmaps.datasets.load_dataset('taxi_rides')
# proxies = {'http': '10.2.1.240:8123', 'https': '10.2.1.240:8123'}
# m = gmaps.Map(proxies=proxies)
# m.add_layer(gmaps.Heatmap(data=data))

# Get Point lat&lon
location = MeshCodeUtility.geocoding2('qingdao')

# Get Polygon lat&lon
polygons = []
polygons.append([54200380, MeshCodeUtility.Mesh2coordinate(54200380)])
polygons.append([54200381, MeshCodeUtility.Mesh2coordinate(54200381)])
polygons.append([54200382, MeshCodeUtility.Mesh2coordinate(54200382)])
polygons.append([54200383, MeshCodeUtility.Mesh2coordinate(54200383)])
polygons.append([54200384, MeshCodeUtility.Mesh2coordinate(54200384)])
polygons.append([54200385, MeshCodeUtility.Mesh2coordinate(54200385)])
polygons.append([54200386, MeshCodeUtility.Mesh2coordinate(54200386)])
polygons.append([54200387, MeshCodeUtility.Mesh2coordinate(54200387)])
polygons.append([54200388, MeshCodeUtility.Mesh2coordinate(54200388)])
polygons.append([54200389, MeshCodeUtility.Mesh2coordinate(54200389)])

f_polygons = []
for ply in polygons:
    m_polygons = Polygon([ply[1]])           # []が必須
    f_polygons.append(Feature(geometry=m_polygons, id=ply[0]))
features = FeatureCollection(f_polygons)      # []が必須

dump = geojson.dumps(features)
geoJsonData = geojson.loads(dump)
print(geoJsonData)

# mesh_geo = r'file2/meshs.json'
# f = open(mesh_geo, 'w')
# f.write(str(features))

# Create JS MAP
# http://www.dataguru.cn/article-8747-1.html
map_osm = folium.Map(location=location)

# マーカー追加
folium.Marker(location=location, popup='QingDao').add_to(map_osm)
marker = folium.RegularPolygonMarker(location=[36.184488, 120.434222], fill_color='#43d9de',
                                    radius=11, popup='百通馨苑五区', number_of_sides=0)
map_osm.add_children(child=marker)

# Mesh追加
# folium.GeoJson(
#     geoJsonData,
#     style_function=lambda feature: {
#         'color': 'black',
#         'weight': 1
#     }
# ).add_to(map_osm)
threshold_scale = [1, 30, 50, 70, 90, 100]
map_osm.choropleth(geo_str=geoJsonData, data=mesh_data,
               columns=['mesh_cd', 'sales'], key_on='feature.id',
               fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2, # colorbrewer: http://colorbrewer2.org/
               legend_name='人口', threshold_scale=threshold_scale)

map_osm.save('file2/osm.html')


# state_geo = r'file2/us-states.json'
# state_unemployment = r'file2/US_Unemployment_Oct2012.csv'
# state_data = pd.read_csv(state_unemployment)
#
# # Let Folium determine the scale
# map = folium.Map(location=[48, -102], zoom_start=3)
#
# threshold_scale = [1, 3, 5, 7, 9, 10]
# map.choropleth(geo_path=state_geo, data=state_data,
#                columns=['State', 'Unemployment'], key_on='feature.id',
#                fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
#                legend_name='Unemployment Rate (%)', threshold_scale=threshold_scale)
#

# map.save('file2/osm.html')

