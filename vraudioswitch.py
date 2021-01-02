from sys import path
import psutil
import time, json, os

for service in psutil.process_iter():
    data = service.as_dict()

if os.path.isdir('./tests') == False:
    os.mkdir('./tests')

out = open('.\\tests\\output.json', 'w')
out.write(str(json.dumps(data, indent=2)))
out.close()
