import sys
import json

for line in sys.stdin:

    json_data=json.loads(line)

    print(json_data["Naam"])
