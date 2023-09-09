import json

json_file = open('Sergey_Kuznetsov.json', 'r')
json_data = json.load(json_file)
json_file.close()

x_values = []
for i in json_data['measurements']:
    x_value = i['x']
    x_values.append(x_value)

y_values = []
for i in json_data['measurements']:
    y_value = i['y']
    y_values.append(y_value)

print(x_values)
print(y_values)
