import json

json_file = open('Sergey_Kuznetsov.json', 'r')
json_data = json.load(json_file)
json_file.close()

# with open('Sergey_Kuznetsov.json') as user_file:
#     json_data = user_file.read()
# print(file_contents)

x_values = json_data['measurements'][0]['x']
y_values = json_data['measurements'][0]['y']

print(x_values)
print(y_values)