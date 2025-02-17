import time
def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        print("it take 4 sec to calculate")
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_sum(a, b):
    time.sleep(4)
    return(a + b)

print(long_sum(5, 6))
print(long_sum(7, 8))
print(long_sum(5, 6))