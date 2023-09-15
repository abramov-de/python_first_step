import json
import matplotlib.pyplot as plt
from math import cos, sin
import jmespath

json_file = open('Sergey_Kuznetsov.json', 'r')
json_data = json.load(json_file)
json_file.close()

x_values = []
y_values = []
angles = []
dists = []
Y = []

for i in json_data['measurements']:
    if i['mode'] == 'calibration':
        continue
    Y.append(i['Y'])

Y = list(set(Y))

center1 = []
center2 = []
center3 = []
center4 = []
center5 = []
center6 = []
center7 = []
center8 = []
center9 = []

for i in json_data['measurements']:
    if i['Y'] == Y[0]:
        center1.append(i['distance'])
    if i['Y'] == Y[1]:
        center2.append(i['distance'])
    if i['Y'] == Y[2]:
        center3.append(i['distance'])
    if i['Y'] == Y[3]:
        center4.append(i['distance'])
    if i['Y'] == Y[4]:
        center5.append(i['distance'])
    if i['Y'] == Y[5]:
        center6.append(i['distance'])
    if i['Y'] == Y[6]:
        center7.append(i['distance'])
    if i['Y'] == Y[7]:
        center8.append(i['distance'])
    if i['Y'] == Y[8]:
        center9.append(i['distance'])

print(Y[0], center1)
print(Y[1], center2)
print(Y[2], center3)
print(Y[3], center4)
print(Y[4], center5)
print(Y[5], center6)
print(Y[6], center7)
print(Y[7], center8)
print(Y[8], center9)



# for i in json_data['measurements']:
#     x_value = i['x']
#     y_value = i['y']
#     if i['mode'] == 'calibration':
#         continue
#     if i['Y'] == i+1['Y']:
#         dists.append(i['distance'])
#     elif i['Y'] != i+1['Y']:


#     if x_value == 0.1895300876:
#         angle = i['angle']
#         angles.append(angle)
#         distance = i['distance']  # if mode == calibration
#         if distance is None:
#             distance = 0
#         dists.append(distance)
#         x_values.append(x_value + (cos(angle) * distance))
#         y_values.append(y_value + (sin(angle) * distance))
#     else:
#         break
#
# ang_dist = list(zip(angles, dists, x_values, y_values))
# sort_ang_dist = sorted(ang_dist)
#
# print(angles)
# print(dists)
# print(ang_dist)
# print(sort_ang_dist)
# print(x_values)
# print(y_values)
# print("angles type:", type(angles))
# print("dists type:", type(dists))
# print("ang_dist type:", type(ang_dist))
# print("sort_ang_dist type:", type(sort_ang_dist))
# print("x_values type:", type(x_values))
# print("y_values type:", type(y_values))
#
# for i in range(len(sort_ang_dist)):
#     plt.scatter(sort_ang_dist[i][2], sort_ang_dist[i][3])
#
# plt.show()

# to do: массив цветовых центров (xyY), разбить на центры, 32 измерения в каждом центре, должно быть по 4 штуки для каждого угла
# в табл 8 на 4, 8 направл
# испытуемые - цвет центы - попытки(измерения) - 8 измерений для разн углов (из них строится эллипс)
