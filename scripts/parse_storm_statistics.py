import csv
import json

track = []

with open('../datasets/storm_track_statistics.txt','rb') as tsvin:
    tsvin = csv.DictReader(tsvin, delimiter='\t')
    for row in tsvin:
        lon = float(row['Lon'][0:5])
        lat = float(row['Lat'][0:4])
        day = row['Date'][0:2]
        time = row['Time'][0:5]
        category = row['Category']
        timestamp = "2017-09-{0}T{1}:00Z".format(day,time)
        track.append({'lon':lon,'lat':lat,'timestamp':timestamp,'category':category})

print json.dumps(track)
