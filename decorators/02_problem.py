def debug(func):
    def wrapper(*args, **kwargs):
        all_args = ", ".join(str(arg) for arg in args)
        all_kwargs = ", ".join(f'{k} = {v}' for k, v in kwargs.items())
        print(f"{func.__name__} called with arguments : {all_args} and {all_kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def findPower(a : int, b = 2):
    return a ** b

print(findPower(35, b = 3))