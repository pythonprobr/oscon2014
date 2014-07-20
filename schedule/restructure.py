# restructure.py
# handling of OSCON 2014 schedule data feed

import json
import pickle

FEED_NAME = 'osconfeed.json'
SCHEDULE_NAME = 'schedule.pickle'


def list2dict(record_list):
    result = {}
    for record in record_list:
        key = record['serial']
        assert key not in result
        result[key] = record
    return result

with open(FEED_NAME, encoding='utf-8') as fp:
    feed = json.load(fp)

schedule = feed['Schedule']
new_schedule = {}

for key, record_list in sorted(schedule.items()):
    print('%12s: %3d items' % (key, len(record_list)))
    if key != 'conferences':
        new_schedule[key] = list2dict(record_list)

with open(SCHEDULE_NAME, 'wb') as fp:
    feed = pickle.dump(new_schedule, fp)

print('saved', SCHEDULE_NAME)
