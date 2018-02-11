import datetime
import math
import json

f = open('../datasets/drifer_data.dat').read()

features = []

for counter, line in enumerate(f.split("\n")):
    if counter < 3:
        continue
    l = line.split()
    if len(l) < 7:
        continue
    id = l[0]
    month = int(l[1])
    day_dec = float(l[2])
    year = int(l[3])
    lat = l[4]
    lon = l[5]

    day = int(math.floor(day_dec))
    hour = (day_dec * 24) % 24
    minute = (day_dec * 24 *60) % 60
    
    timestamp = int(datetime.datetime(year,month,day,int(hour),int(minute)).strftime('%s'))
    if timestamp < 1505574000 - 60 * 60 * 24 * 7 or timestamp > 1506805200 + 60 * 60 * 24 * 7:
        continue
    features.append({
        'type':'Feature',
        'geometry':{
            'type':'Point',
            'coordinates':[lon,lat]
        },
        'properties':{
            'timestamp':int(timestamp) * 1000
        }
    })

print json.dumps({'type':'FeatureCollection','features':features})
