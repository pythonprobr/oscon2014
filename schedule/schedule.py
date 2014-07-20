# schedule.py
# handling of OSCON 2014 schedule data feed

"""

    >>> talk = database['events'][34108]
    >>> talk  # doctest: +ELLIPSIS
    <schedule.Record object at 0x...>
    >>> talk.name
    'Idiomatic APIs with the Python Data Model'
    >>> talk.venue_serial
    1465

"""

import pickle

SCHEDULE_NAME = 'schedule.pickle'


def load():
    with open(SCHEDULE_NAME, 'rb') as fp:
        schedule = pickle.load(fp)

    result = {}
    for collection in 'events', 'speakers', 'venues':
        result[collection] = {key: Record(**value)
                              for key, value in schedule[collection].items()}

    return result


class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

database = load()
