# schedule_refs.py
# handling of OSCON 2014 schedule data feed with
# automatic retrieval of referenced objects

"""

    >>> talk = database['events'][34108]
    >>> talk  # doctest: +ELLIPSIS
    <schedule_refs.Event object at 0x...>
    >>> talk.name
    'Idiomatic APIs with the Python Data Model'
    >>> talk.venue_serial
    1465
    >>> talk.venue  # doctest: +ELLIPSIS
    <schedule_refs.Record object at 0x...>
    >>> talk.venue.name
    'E145'
    >>> talk.first_speaker.name
    'Luciano Ramalho'

"""

import pickle

SCHEDULE_NAME = 'schedule.pickle'


def load(verbose=False):
    with open(SCHEDULE_NAME, 'rb') as fp:
        schedule = pickle.load(fp)

    if verbose:
        for key, record_list in sorted(schedule.items()):
            print('%12s: %3d items' % (key, len(record_list)))

    result = {}
    for collection in 'events', 'speakers', 'venues':
        if collection == 'events':
            record_class = Event
        else:
            record_class = Record
        result[collection] = {key: record_class(**value)
                              for key, value in schedule[collection].items()}

    return result


class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


class Event(Record):

    @property
    def venue(self):
        key = self.venue_serial
        return database['venues'][key]

    @property
    def first_speaker(self):
        key = self.speakers[0]
        return database['speakers'][key]

database = load()
