import json
import matplotlib.pyplot as plt
from math import cos, sin
import jmespath

json_file = open('Sergey_Kuznetsov.json', 'r')
json_data = json.load(json_file)
json_file.close()

x_values = []
y_values = []
# angles = []
# dists = []
Y = []

for i in json_data['measurements']:
    if i['mode'] == 'calibration':
        continue
    Y.append(i['Y'])

Y = list(set(Y))

dists1 = []
angles1 = []
dists2 = []
angles2 = []
dists3 = []
angles3 = []
dists4 = []
angles4 = []
dists5 = []
angles5 = []
dists6 = []
angles6 = []
dists7 = []
angles7 = []
dists8 = []
angles8 = []
dists9 = []
angles9 = []

for i in json_data['measurements']:
    if i['Y'] == Y[0]:
        dists1.append(i['distance'])
        angles1.append(i['angle'])
    if i['Y'] == Y[1]:
        dists2.append(i['distance'])
        angles2.append(i['angle'])
    if i['Y'] == Y[2]:
        dists3.append(i['distance'])
        angles3.append(i['angle'])
    if i['Y'] == Y[3]:
        dists4.append(i['distance'])
        angles4.append(i['angle'])
    if i['Y'] == Y[4]:
        dists5.append(i['distance'])
        angles5.append(i['angle'])
    if i['Y'] == Y[5]:
        dists6.append(i['distance'])
        angles6.append(i['angle'])
    if i['Y'] == Y[6]:
        dists7.append(i['distance'])
        angles7.append(i['angle'])
    if i['Y'] == Y[7]:
        dists8.append(i['distance'])
        angles8.append(i['angle'])
    if i['Y'] == Y[8]:
        dists9.append(i['distance'])
        angles9.append(i['angle'])

center1 = list(zip(dists1, angles1))
center2 = list(zip(dists2, angles2))
center3 = list(zip(dists3, angles3))
center4 = list(zip(dists4, angles4))
center5 = list(zip(dists5, angles5))
center6 = list(zip(dists6, angles6))
center7 = list(zip(dists7, angles7))
center8 = list(zip(dists8, angles8))
center9 = list(zip(dists9, angles9))

print(Y[0], dists1)
print(Y[0], angles1)
print(Y[1], dists2)
print(Y[1], angles2)
print(Y[2], dists3)
print(Y[2], angles3)
print(Y[3], dists4)
print(Y[3], angles4)
print(Y[4], dists5)
print(Y[4], angles5)
print(Y[5], dists6)
print(Y[5], angles6)
print(Y[6], dists7)
print(Y[6], angles7)
print(Y[7], dists8)
print(Y[7], angles8)
print(Y[8], dists9)
print(Y[8], angles9)
print(center1)
print(center2)
print(center3)
print(center4)
print(center5)
print(center6)
print(center7)
print(center8)
print(center9)




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
