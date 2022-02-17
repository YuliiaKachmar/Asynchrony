def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner()


class BlaBlaException(Exception):
    pass


@coroutine
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except BlaBlaException:
            print('Done')
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)

    return average
