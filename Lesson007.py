# -*-encoding:utf-8 -*-
# file:class.py
import numpy as np
import pandas as pd
import json


txt = open('file/dict.txt').read()
jsn = "{%(txt)s}" % vars()
reader = json.JSONDecoder()
points = reader.decode(jsn)

'''''
输入一个测试点，这个点通过GPS产生
建议输入三个点测试
在信息学馆内的点:123.4263790000,41.7740520000 123.42699,41.773592
在图书馆内的点:  123.4261550000,41.7726740000 123.42571,41.772499 123.425984,41.772919
不在二者内的点:  123.4246270000,41.7738130000
在信息学馆外包矩形内，但不在信息学馆中的点：123.4264060000,41.7737860000
'''
# lat = raw_input(please input lat)
# lng = raw_input(please input lng)

lat = 41.5095766
lng = 140.010004
point = Point(lat, lng)

debug = input("请输入debug: ")
if debug == '1':
    debug = True
else:
    debug = False

# 求外包矩形
def getPolygonBounds(points):
    length = len(points)
    # top down left right 都是point类型
    top = down = left = right = points[0]
    for i in range(1, length):
        if points[i].lng > top.lng:
            top = points[i]
        elif points[i].lng < down.lng:
            down = points[i]
        else:
            pass
        if points[i].lat > right.lat:
            right = points[i]
        elif points[i].lat < left.lat:
            left = points[i]
        else:
            pass

    point0 = Point(left.lat, top.lng)
    point1 = Point(right.lat, top.lng)
    point2 = Point(right.lat, down.lng)
    point3 = Point(left.lat, down.lng)
    polygonBounds = [point0, point1, point2, point3]
    return polygonBounds

# 测试求外包矩形的一段函数
# if debug:
#     poly1 = getPolygonBounds(points[0])
#     print("第一个建筑的外包是：")
#     for i in range(0, len(poly1)):
#         poly1[i].show()
#     poly2 = getPolygonBounds(points[1])
#     print("第二个建筑的外包是：")
#     for i in range(0, len(poly2)):
#         poly2[i].show()


# 判断点是否在外包矩形外
def isPointInRect(point, polygonBounds):
    if ((point.lng >= polygonBounds[3].lng)
        and (point.lng <= polygonBounds[0].lng)
        and (point.lat >= polygonBounds[3].lat)
        and (point.lat <= polygonBounds[2].lat)):
       return True
    else:
        return False

# 测试是否在外包矩形外的代码
# if debug:
#     if(isPointInRect(point, poly1)):
#         print("在信息外包矩形内")
#     else:
#         print("在信息外包矩形外")
#
#     if(isPointInRect(point, poly2)):
#         print("在图书馆外包矩形内")
#     else:
#         print("在图书馆外包矩形外")


# 采用射线法，计算测试点是否任意一个建筑内
def isPointInPolygon(point, points):
    # 定义在边界上或者在顶点都建筑内
    Bound = Vertex = True
    count = 0
    precision = 2e-10

    # 首先求外包矩形
    polygonBounds = getPolygonBounds(points)

    # 然后判断是否在外包矩形内，如果不在，直接返回false
    if not isPointInRect(point, polygonBounds):
        if debug:
            print("在外包矩形外")
        return False
    else:
        if debug:
            print("在外包矩形内")

    length = len(points)
    p = point
    p1 = points[0]
    for i in range(1, length):
        if p.lng == p1.lng and p.lat == p1.lat:
            if debug:
                print("Vertex1")
            return Vertex

        p2 = points[i % length]
        if p.lng == p2.lng and p.lat == p2.lat:
            if debug:
                print("Vertex2")
            return Vertex

        # if debug:
        #     print(i-1, i)
        #     print("p:")
        #     p.show()
        #     print("p1:")
        #     p1.show()
        #     print("p2:")
        #     p2.show()

        if p.lng < min(p1.lng, p2.lng) or \
            p.lng > max(p1.lng, p2.lng) or \
            p.lat > max(p1.lat, p2.lat):
            p1 = p2
            # if debug:
            #     print("Outside")
            continue

        elif (p.lng > min(p1.lng, p2.lng)) and (p.lng < max(p1.lng, p2.lng)):
            if p1.lat == p2.lat:
                if (p.lat == p1.lat) and (p.lng > min(p1.lng, p2.lng)) and (p.lng < max(p1.lng, p2.lng)):
                    return Bound
                else:
                    count += 1
                    if debug:
                        print("count1:", count)
                    continue
            if debug:
                print("into left or right")

            a = p2.lng - p1.lng
            b = p1.lat - p2.lat
            c = p2.lat * p1.lng - p1.lat * p2.lng
            d = a * p.lat + b * p.lng + c
            if p1.lng < p2.lng and p1.lat > p2.lat or \
               p1.lng < p2.lng and p1.lat < p2.lat:
                if d < 0:
                    count += 1
                    if debug:
                        print("count2:", count)
                elif d > 0:
                    p1 = p2
                    continue
                elif abs(p.lng-d) < precision:
                    return Bound
            else:
                if d < 0:
                    p1 = p2
                    continue
                elif d > 0:
                    count += 1
                    if debug:
                        print("count3:", count)
                elif abs(p.lng-d) < precision:
                    return Bound
        else:
            if p1.lng == p2.lng:
                if (p.lng == p1.lng) and (p.lat > min(p1.lat, p2.lat)) and (p.lat < max(p1.lat, p2.lat)):
                   return Bound
            else:
                p3 = points[(i+1) % length]
                if (p.lng < min(p1.lng, p3.lng)) or (p.lng > max(p1.lng, p3.lng)):
                    count += 2
                    if debug:
                        print("count4:", count)
                else:
                    count += 1
                    if debug:
                        print("count5:", count)
        p1 = p2
    if count % 2 == 0:
        return False
    else:
        return True

length = len(points)
flag = 0
for i in range(length):
    if isPointInPolygon(point, points[i]):
        print("你刚才输入的点在第 %d 个建筑里" % (i+1))
        # print("然后根据i值，可以读出建筑名，或者修改传入的points参数")
        break
    else:
        flag += 1

if flag == length:
    print("在头 %d 建筑外" % (i+1))
