class MyDecorator:
    def __init__(self, n):
        self.count = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("*"*self.count)
            func(*args, **kwargs)
            print("*"*self.count)
        return wrapper

@MyDecorator(5)
def f1(x):
    print(f"Call f1 = {x**2}")

f1(3)