import json

a = {"location":{"name":"Auckland","region":"","country":"New Zealand","lat":-36.87,"lon":174.77,"tz_id":"Pacific/Auckland",
  "localtime_epoch":1517803632,"localtime":"2018-02-05 17:07"},
    "current":{"last_updated_epoch":1517802732,"last_updated":"2018-02-05 16:52",
    "temp_c":24.9,"temp_f":76.8,"is_day":1,
    }}

b = json.dumps(a) #//json(dict) to string
# c = json.loads(a)
# print(b)
c = json.loads(b) # string parse to json dict
# print(type(b))
# print(type(c))
# print(b[0])
# print(c)
# print(c['location']['name'])
print(a.get('location').get('name'))
# print(c)
