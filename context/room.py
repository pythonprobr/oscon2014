"""
    >>> with Room() as r:  # doctest: +ELLIPSIS
    ...     print(r)
    entering the room
    <room.Room object at 0x...>
    exiting the room with no incident.


"""


class Room:

    def __init__(self, silent=False):
        self.silent = silent

    def __enter__(self):
        print('entering the room')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print('exiting the room with no incident.')
        else:
            print('exiting with {}'.format((exc_type, exc_value, traceback)))
        if self.silent:
            return True  # suppress exception propagation
