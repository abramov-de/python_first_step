import json
import matplotlib.pyplot as plt
from math import cos, sin

json_file = open('Sergey_Kuznetsov.json', 'r')
json_data = json.load(json_file)
json_file.close()

x_values = []
y_values = []
angles = []
dists = []
for i in json_data['measurements']:
    x_value = i['x']
    y_value = i['y']
    if x_value == 0.1895300876:
        angle = i['angle']
        angles.append(angle)
        distance = i['distance']
        if distance is None:
            distance = 0
        dists.append(distance)
        x_values.append(x_value + (cos(angle) * distance))
        y_values.append(y_value + (sin(angle) * distance))
    else:
        break

ang_dist = list(zip(angles, dists))
sort_ang_dist = sorted(ang_dist)

print(angles)
print(dists)
print(ang_dist)
print(sort_ang_dist)
print(x_values)
print(y_values)
print("angles type:", type(angles))
print("dists type:", type(dists))
print("ang_dist type:", type(ang_dist))
print("sort_ang_dist type:", type(sort_ang_dist))
print("x_values type:", type(x_values))
print("y_values type:", type(y_values))
