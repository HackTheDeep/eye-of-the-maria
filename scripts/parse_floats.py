from netCDF4 import Dataset, MFDataset
import glob
import numpy
import json
import warnings

warnings.simplefilter('error', UserWarning)

features = []

def avg_to_json(arr):
    avg = numpy.average(arr)
    try:
        return float(avg)
    except:
        return None

for filename in glob.glob("FLOATS/*"):
    rootgroup = Dataset(filename,'r')
    ymd = filename[7:15]
    z = zip(rootgroup.variables['PLATFORM_NUMBER'][:],rootgroup.variables['LATITUDE'][:],rootgroup.variables['LONGITUDE'][:],rootgroup.variables['TEMP'][:], rootgroup.variables['PRES'][:], rootgroup.variables['PSAL'][:])
    for thing in z:
        latitude = float(thing[1])
        longitude = float(thing[2])
        mean_temp = avg_to_json(thing[3])
        mean_pres = avg_to_json(thing[4])
        mean_psal = avg_to_json(thing[5])
        platform_number = ''.join(list(thing[0][:-1]))
        feature = {'type':'Feature','geometry':{'type':'Point','coordinates':[longitude,latitude]},'properties':{'platform_number':platform_number,'temp':mean_temp,'pres':mean_pres,'psal':mean_psal,'ymd':ymd}}
        features.append(feature)

print json.dumps({'type':'FeatureCollection','features':features})
