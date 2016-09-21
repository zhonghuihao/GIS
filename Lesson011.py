from module_mesh import MeshCodeUtility
import sys, urllib.request, json


# polygon = [(120.661475, 36.290097), (120.698554, 36.199278), (120.881202, 36.210359), (120.944373, 36.295632)]
# print(MeshCodeUtility.mesh1polygon(polygon))

url = 'http://api.map.baidu.com/api?v=2.0&qt=s'
query = '&wd=qingdao'
output = '&output=json'
ak = '&ak=1XjLLEhZhQNUzd93EjU5nOGQ'
url = url + query + output + ak

print(url)
resp = urllib.request.urlopen(url)
content = resp.read()

if(content):
    print(content)

