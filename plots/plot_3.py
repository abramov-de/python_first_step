import json
import matplotlib.pyplot as plt
from math import cos, sin

json_file = open('Sergey_Kuznetsov.json', 'r')
json_data = json.load(json_file)
json_file.close()

x_values = []
for i in json_data['measurements']:
    x_value = i['x']
    angle_x = i['angle']
    distance_x = i['distance']
    if distance_x is None:
        distance_x = 0
    x_values.append(x_value + (cos(angle_x) * distance_x))

y_values = []
for i in json_data['measurements']:
    y_value = i['y']
    angle_y = i['angle']
    distance_y = i['distance']
    if distance_y is None:
        distance_y = 0
    y_values.append(y_value + (sin(angle_y) * distance_y))

# print(x_values)
# print(y_values)
# print(type(x_values))
# print(type(y_values))

plt.scatter(x_values, y_values)
plt.show()
