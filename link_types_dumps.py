# script to serialize link type lists to JSON
import csv
import json


def to_json(csvobj):
    """serialize to JSON"""

    # skip CSV header
    csvobj.next()
    payload = []
    for row in csvobj:
        payload.append({'link_type': row[0], 'description': row[1]})

    return json.dumps(payload)

# main
with open('link_types.csv') as csvfile:
    CSV_READER = csv.reader(csvfile)
    PAYLOAD = to_json(CSV_READER)

print PAYLOAD
