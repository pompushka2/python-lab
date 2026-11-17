import datetime
import functools

def log_calls(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            time=datetime.datetime.now()
            with open(filename,'a') as f:
                f.write(f"{time}:{func.__name__}({args})\n")
                return func(*args)
            return func
        return wrapper
    return decorator

@log_calls("calls")
def hello():
    return "Hello world"


hello()
