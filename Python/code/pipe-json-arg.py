import sys
import json
import argparse

parser = argparse.ArgumentParser(
    description="Filter 1 element uit JSON input"
)

parser.add_argument("--key", required=True, type=str)

args = parser.parse_args()

for line in sys.stdin:

    json_data=json.loads(line)

    print(json_data[args.key])
