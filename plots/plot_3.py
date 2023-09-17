import json
import pandas as pd

json_file = open('Sergey_Kuznetsov.json', 'r')
json_data = json.load(json_file)
json_file.close()

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

x_origin1 = []
y_origin1 = []

x_origin2 = []
y_origin2 = []

x_origin3 = []
y_origin3 = []

x_origin4 = []
y_origin4 = []

x_origin5 = []
y_origin5 = []

x_origin6 = []
y_origin6 = []

x_origin7 = []
y_origin7 = []

x_origin8 = []
y_origin8 = []

x_origin9 = []
y_origin9 = []


for i in json_data['measurements']:

    if i['Y'] == Y[0]:
        if i['mode'] == 'calibration':
            continue
        dists1.append(i['distance'])
        angles1.append(i['angle'])
        x_origin1.append(i['x'])
        y_origin1.append(i['y'])

    if i['Y'] == Y[1]:
        if i['mode'] == 'calibration':
            continue
        dists2.append(i['distance'])
        angles2.append(i['angle'])
        x_origin2.append(i['x'])
        y_origin2.append(i['y'])

    if i['Y'] == Y[2]:
        if i['mode'] == 'calibration':
            continue
        dists3.append(i['distance'])
        angles3.append(i['angle'])
        x_origin3.append(i['x'])
        y_origin3.append(i['y'])

    if i['Y'] == Y[3]:
        if i['mode'] == 'calibration':
            continue
        dists4.append(i['distance'])
        angles4.append(i['angle'])
        x_origin4.append(i['x'])
        y_origin4.append(i['y'])

    if i['Y'] == Y[4]:
        if i['mode'] == 'calibration':
            continue
        dists5.append(i['distance'])
        angles5.append(i['angle'])
        x_origin5.append(i['x'])
        y_origin5.append(i['y'])

    if i['Y'] == Y[5]:
        if i['mode'] == 'calibration':
            continue
        dists6.append(i['distance'])
        angles6.append(i['angle'])
        x_origin6.append(i['x'])
        y_origin6.append(i['y'])

    if i['Y'] == Y[6]:
        if i['mode'] == 'calibration':
            continue
        dists7.append(i['distance'])
        angles7.append(i['angle'])
        x_origin7.append(i['x'])
        y_origin7.append(i['y'])

    if i['Y'] == Y[7]:
        if i['mode'] == 'calibration':
            continue
        dists8.append(i['distance'])
        angles8.append(i['angle'])
        x_origin8.append(i['x'])
        y_origin8.append(i['y'])

    if i['Y'] == Y[8]:
        if i['mode'] == 'calibration':
            continue
        dists9.append(i['distance'])
        angles9.append(i['angle'])
        x_origin9.append(i['x'])
        y_origin9.append(i['y'])


dists1 = [item if item else 0 for item in dists1]
dists2 = [item if item else 0 for item in dists2]
dists3 = [item if item else 0 for item in dists3]
dists4 = [item if item else 0 for item in dists4]
dists5 = [item if item else 0 for item in dists5]
dists6 = [item if item else 0 for item in dists6]
dists7 = [item if item else 0 for item in dists7]
dists8 = [item if item else 0 for item in dists8]
dists9 = [item if item else 0 for item in dists9]

Y_0 = [Y[0] for _ in range(len(dists1))]
Y_1 = [Y[1] for _ in range(len(dists2))]
Y_2 = [Y[2] for _ in range(len(dists3))]
Y_3 = [Y[3] for _ in range(len(dists4))]
Y_4 = [Y[4] for _ in range(len(dists5))]
Y_5 = [Y[5] for _ in range(len(dists6))]
Y_6 = [Y[6] for _ in range(len(dists7))]
Y_7 = [Y[7] for _ in range(len(dists8))]
Y_8 = [Y[8] for _ in range(len(dists9))]

center1 = list(zip(Y_0, dists1, angles1))
center2 = list(zip(Y_1, dists2, angles2))
center3 = list(zip(Y_2, dists3, angles3))
center4 = list(zip(Y_3, dists4, angles4))
center5 = list(zip(Y_4, dists5, angles5))
center6 = list(zip(Y_5, dists6, angles6))
center7 = list(zip(Y_6, dists7, angles7))
center8 = list(zip(Y_7, dists8, angles8))
center9 = list(zip(Y_8, dists9, angles9))

center1.sort(key=lambda x: x[-1])
center2.sort(key=lambda x: x[-1])
center3.sort(key=lambda x: x[-1])
center4.sort(key=lambda x: x[-1])
center5.sort(key=lambda x: x[-1])
center6.sort(key=lambda x: x[-1])
center7.sort(key=lambda x: x[-1])
center8.sort(key=lambda x: x[-1])
center9.sort(key=lambda x: x[-1])


df1 = pd.DataFrame(center1, columns=['Color center', 'Distance', 'Angle'])
df2 = pd.DataFrame(center2, columns=['Color center', 'Distance', 'Angle'])
df3 = pd.DataFrame(center3, columns=['Color center', 'Distance', 'Angle'])
df4 = pd.DataFrame(center4, columns=['Color center', 'Distance', 'Angle'])
df5 = pd.DataFrame(center5, columns=['Color center', 'Distance', 'Angle'])
df6 = pd.DataFrame(center6, columns=['Color center', 'Distance', 'Angle'])
df7 = pd.DataFrame(center7, columns=['Color center', 'Distance', 'Angle'])
df8 = pd.DataFrame(center8, columns=['Color center', 'Distance', 'Angle'])
df9 = pd.DataFrame(center9, columns=['Color center', 'Distance', 'Angle'])


print("Color center 1 :", "\n\n", df1, "\n", "Color center 2 :", "\n\n", df2, "\n",
      "Color center 3 :", "\n\n", df3, "\n", "Color center 4 :", "\n\n", df4, "\n",
      "Color center 5 :", "\n\n", df5, "\n", "Color center 6 :", "\n\n", df6, "\n",
      "Color center 7 :", "\n\n", df7, "\n", "Color center 8 :", "\n\n", df8, "\n",
      "Color center 9 :", "\n\n", df9, "\n")

with open('color_centers.txt', 'w') as f:
    print("Color center 1 :", "\n\n", df1, "\n", "Color center 2 :", "\n\n", df2, "\n",
          "Color center 3 :", "\n\n", df3, "\n", "Color center 4 :", "\n\n", df4, "\n",
          "Color center 5 :", "\n\n", df5, "\n", "Color center 6 :", "\n\n", df6, "\n",
          "Color center 7 :", "\n\n", df7, "\n", "Color center 8 :", "\n\n", df8, "\n",
          "Color center 9 :", "\n\n", df9, "\n", file=f)

print(x_origin9)
print(y_origin9)

print(x_origin1)
print(y_origin1)


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
