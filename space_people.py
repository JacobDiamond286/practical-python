import requests

people = requests.get('httpL//api.open-notify.org/astros.json')
json = people.json()

print(json)

print('The people currently in space are:')
for p in json['people']:
    print(p['name'])