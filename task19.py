import functools
res = {}
def cache(func):
    @functools.wraps(func)
    def wrapper(*args):
        key = args
        if key not in res:
            res[key] = func(*args)
            print(f"[cache-write] {func.__name__}{args}")
        else:
            print(f"[cache-hit] {func.__name__}{args}")
        return res[key]

    return wrapper


@cache
def pow(a, b):
    return a**b


pow(2, 3)
pow(2, 3)