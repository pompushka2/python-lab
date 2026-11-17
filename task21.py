import time
res= {}

def timing(func):
    def wrapper(*args):
        start = time.perf_counter()
        res = func(*args)
        end = time.perf_counter()
        print(f" время выполнения: {end - start:.8f} c")
        return res
    return wrapper

@timing
def pow(a, b):
    return a ** b

pow(2, 3)
pow(2, 3)