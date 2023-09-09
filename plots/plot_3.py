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
    if i['distance'] == 'null':
        distance_x = 0
    else:
        distance_x = i['distance']
    x_values.append(x_value + (cos(angle_x) * distance_x))

y_values = []
for i in json_data['measurements']:
    y_value = i['y']
    angle_y = i['angle']
    distance_y = i['distance']
    y_values.append(y_value + (sin(angle_y) * distance_y))

plt.plot(x_values, y_values)
plt.show()

print(x_values)
print(y_values)
print(type(x_values))
print(type(y_values))
