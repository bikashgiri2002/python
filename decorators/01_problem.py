import time
def timefunction(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} is take {end_time - start_time} seconds to run')
        return result
    return wrapper

@timefunction
def exampleFunction(n):
    time.sleep(n)
    print('completed')

exampleFunction(4)