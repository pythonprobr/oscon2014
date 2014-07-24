"""
    >>> with room() as r:  # doctest: +ELLIPSIS
    ...     print(r)
    entering the room
    <function room at 0x...>
    exiting the room with no incident.


"""

from contextlib import contextmanager

@contextmanager
def room(silent=False):
    print('entering the room')
    try:
        yield room
    except Exception as exc:
        traceback = exc.__traceback__
        print('exiting with {}'.format((type(exc), exc, traceback)))
        if not silent:
            raise
    else:
        print('exiting the room with no incident.')
