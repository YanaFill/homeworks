class Dynamic:
    def __init__(self):
        self._attributes = {}

    def __getattr__(self, name: str):
        print(f"Call __getattr__ {name}")
        if name in self._attributes:
            return self._attributes[f"{name}"]
        else:
            raise AttributeError(f"Dynamic has no attribute '{name}'")

    def __setattr__(self, name, value):
        print(f"Call __setattr__ with {name=}, {value=}")
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            self._attributes[f"{name}"] = value

    def __delattr__(self, item):
        del self._attributes[item]

    def __getattribute__(self, name):
        print(f"Call __getattribute__ with {name=}")
        if name in ('_attributes', '__dict__'):
            return super().__getattribute__(name)
        else:
            if name == "secret":
                raise AttributeError("Access to secret attribute is denied")
            else:
                return super().__getattribute__(name)
dynamic = Dynamic()

print(dynamic.__dict__)
dynamic.name = "John Doe"
print(dynamic.__dict__)
print(dynamic.name)
del dynamic.name
print(dynamic.__dict__)

try:
    print(dynamic.secret)
except AttributeError as e:
    print(e)
