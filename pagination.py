import datetime
import arrow


def num_pagination(init, stop, limit=9):
    while stop >= init:
        _stop = init + limit
        yield init, _stop
        init = _stop + 1


def day_pagination(init: str, stop: str, limit=9):
    init = arrow.get(init, 'YYYY-MM-DD')
    _stop = stop = arrow.get(stop, 'YYYY-MM-DD')
    while stop >= init:
        _stop = init.shift(days=limit)
        yield init.date().__str__(), min([_stop.date().__str__(), stop.date().__str__()])
        init = _stop.shift(days=1)


def minute_pagination(init: str, stop: str, limit_minute=10):
    init = datetime.datetime.strptime(init, '%Y-%m-%d %H:%M:%S')
    stop = datetime.datetime.strptime(stop, '%Y-%m-%d %H:%M:%S')
    while stop >= init:
        _stop = init + datetime.timedelta(minutes=limit_minute)
        yield str(init), min([_stop, stop])
        init = _stop + datetime.timedelta(seconds=1)

for s,e in day_pagination('2023-04-20 16:06:43', '2023-07-20 16:06:53'):
    print(s, e)