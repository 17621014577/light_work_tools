import datetime


def num_pagination(init, stop, limit=9):
    while stop >= init:
        _stop = init + limit
        yield init, _stop
        init = _stop + 1


def day_pagination(init: str, stop: str, limit=9):
    init = datetime.datetime.strptime(init[:10], '%Y-%m-%d')
    _stop = stop = datetime.datetime.strptime(stop[:10], '%Y-%m-%d')
    limit = datetime.timedelta(days=limit)
    while stop >= init:
        _stop = init + limit
        yield str(init), min([_stop, stop])
        init = _stop + datetime.timedelta(days=1)


def minute_pagination(init: str, stop: str, limit_minute=10):
    init = datetime.datetime.strptime(init, '%Y-%m-%d %H:%M:%S')
    stop = datetime.datetime.strptime(stop, '%Y-%m-%d %H:%M:%S')
    while stop >= init:
        _stop = init + datetime.timedelta(minutes=limit_minute)
        yield str(init), min([_stop, stop])
        init = _stop + datetime.timedelta(seconds=1)