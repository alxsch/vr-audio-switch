from sys import path
import psutil
import time, json, os

for service in psutil.process_iter():
    data = service.as_dict()

#thisDir = os.path.curdir
newDir = os.path.relpath(path, './debugs/')

print(newDir)

out = open('output.json', 'w')
out.write(str(json.dumps(data, indent=2)))
out.close()
