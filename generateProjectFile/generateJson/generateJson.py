import json
import sys

f = open("app.json", 'w')

title = sys.argv[1]
versionCode = sys.argv[2]
versionName = sys.argv[3]

data = {"title": title, "versionCode": versionCode, "versionName": versionName}

f.write(json.dumps(data))
