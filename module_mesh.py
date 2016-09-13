import math
import requests
from pygeocoder import Geocoder, GeocoderResult
import geojson
from geojson import Polygon, MultiPolygon
from geojson import GeometryCollection
from geojson import Feature, FeatureCollection


class MeshCodeUtility(object):
    # 代表点経緯度の取得
    @staticmethod
    def geocoding(address):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {'sensor': 'false', 'address': address}
        proxies = {'http': '10.2.1.240:8123', 'https': '10.2.1.240:8123'}

        r = requests.get(url, params=params, proxies=proxies)
        results = r.json()['results']
        location = results[0]['geometry']['location']

        return location

    # 代表点経緯度の取得
    @staticmethod
    def geocoding2(address):
        geocoder = Geocoder()
        geocoder.set_proxy('10.2.1.240:8123')
        result = geocoder.geocode(address, language='ja')
        return result.coordinates

    # 1次メッシュコードの取得
    @staticmethod
    def get_1st_mesh(lat, lon):
        left_operator = int(math.floor(lat * 15 / 10))
        right_operator = int(math.floor(lon - 100))

        # 南西端のlat,lon
        dest_lat = left_operator / 15.0 * 10
        dest_lon = right_operator + 100.0

        src = {"mesh_code": str(left_operator) + str(right_operator), "lat": dest_lat, "lon": dest_lon}
        return src

    # 2次メッシュコードの取得
    @staticmethod
    def get_2nd_mesh(lat, lon):
        base_data = MeshCodeUtility.get_1st_mesh(lat, lon)
        # 2次メッシュは緯度方向5分(5/60=0.08333)区切り
        left_operator = int(math.floor((lat - base_data["lat"]) * 100000 / 8333))
        # 経度方向7分30秒(7/60+30/60/60=0.11666+0.008333=0.1249))区切り
        right_operator = int(math.floor((lon - base_data["lon"]) * 1000 / 125))
        # 南西端のlat,lon
        dest_lat = left_operator * 8333.0 / 100000 + base_data["lat"]
        dest_lon = right_operator * 125.0 / 1000 + base_data["lon"]

        src = {"mesh_code": base_data["mesh_code"]+str(left_operator)+str(right_operator),
               "lat": dest_lat, "lon": dest_lon}
        return src

    # 3次メッシュコードの取得
    @staticmethod
    def get_3rd_mesh(lat, lon):
        base_data = MeshCodeUtility.get_2nd_mesh(lat, lon)

        # 3次メッシュは緯度方向 30秒(30/60/60=0.008333)区切り
        left_operator = int(math.floor((lat - base_data["lat"]) * 1000000 / 8333))
        # 経度方向 45秒(45/60/60=0.0125)区切り
        right_operator = int(math.floor((lon - base_data["lon"]) * 10000 / 125))
        # 南西端のlat,lon
        dest_lat = left_operator * 8333.0 / 1000000 + base_data["lat"]
        dest_lon = right_operator * 125.0 / 10000 + base_data["lon"]

        src = {"mesh_code": base_data["mesh_code"]+str(left_operator)+str(right_operator),
               "lat": dest_lat, "lon": dest_lon}
        return src

    # メッシュから頂点座標を取得
    # input: メッシュコード , output: 座標(経度、緯度)
    def Mesh2coordinate(mesh):

        code12 = ('%-8s' % str(mesh))[0:2]
        code34 = ('%-8s' % str(mesh))[2:4]
        code5 = ('%-8s' % str(mesh))[4]
        code6 = ('%-8s' % str(mesh))[5]
        code7 = ('%-8s' % str(mesh))[6]
        code8 = ('%-8s' % str(mesh))[7]
        code9 = 0
        code10 = 0

        lat1_width = 2 / 3
        lng1_width = 1
        lat2_width = (2 / 3) * (1 / 8)
        lng2_width = 1 / 8
        lat3_width = (2 / 3) * (1 / 8) * (1 / 10)
        lng3_width = (1 / 8) * (1 / 10)
        lat4_width = ''
        lng4_width = ''

        coordinate = []
        # 1次メッシュ
        # 西南座標
        lat1_sw = int(code12) / 1.5
        lng1_sw = int(code34) + 100
        coordinate.append([lng1_sw, lat1_sw])

        # 西北座標
        lat1_nw = lat1_sw + lat1_width
        lng1_nw = lng1_sw
        coordinate.append([lng1_nw, lat1_nw])

        # 東北座標
        lat1_ne = lat1_sw + lat1_width
        lng1_ne = lng1_sw + lng1_width
        coordinate.append([lng1_ne, lat1_ne])

        # 東南座標
        lat1_se = lat1_sw
        lng1_se = lng1_sw + lng1_width
        coordinate.append([lng1_se, lat1_se])

        # 2次メッシュ
        if (code5 != ' ') and (code6 != ' '):
            coordinate = []
            # 西南座標
            lat2_sw = lat1_sw + int(code5) * lat2_width
            lng2_sw = lng1_sw + int(code6) * lng2_width
            coordinate.append([lng2_sw, lat2_sw])

            # 西北座標
            lat2_nw = lat2_sw + lat2_width
            lng2_nw = lng2_sw
            coordinate.append([lng2_nw, lat2_nw])

            # 東北座標
            lat2_ne = lat2_sw + lat2_width
            lng2_ne = lng2_sw + lng2_width
            coordinate.append([lng2_ne, lat2_ne])

            # 東南座標
            lat2_se = lat2_sw
            lng2_se = lng2_sw + lng2_width
            coordinate.append([lng2_se, lat2_se])

            if (code7 != ' ') and (code8 != ' '):
                coordinate = []
                # 西南座標
                lat3_sw = lat2_sw + int(code7) * lat3_width
                lng3_sw = lng2_sw + int(code8) * lng3_width
                coordinate.append([lng3_sw, lat3_sw])

                # 西北座標
                lat3_nw = lat3_sw + lat3_width
                lng3_nw = lng3_sw
                coordinate.append([lng3_nw, lat3_nw])

                # 東北座標
                lat3_ne = lat3_sw + lat3_width
                lng3_ne = lng3_sw + lng3_width
                coordinate.append([lng3_ne, lat3_ne])

                # 東南座標
                lat3_se = lat3_sw
                lng3_se = lng3_sw + lng3_width
                coordinate.append([lng3_se, lat3_se])

        return coordinate
    # GeojsonFile作成
    def Mesh2Geojson(meshs):
        polygons = []
        for mesh_cd in meshs:
            polygons.append([mesh_cd, MeshCodeUtility.Mesh2coordinate(mesh_cd)])

        f_polygons = []
        for ply in polygons:
            m_polygons = Polygon([ply[1]])  # []が必須
            f_polygons.append(Feature(geometry=m_polygons, id=ply[0]))
        features = FeatureCollection(f_polygons)  # []が必須

        dump = geojson.dumps(features)
        geoJsonData = geojson.loads(dump)
        print(geoJsonData)

