import re, pytest


class Descriptor:
    def __init__(self, prefix, min_length=None, max_length=None):
        self.prefix = prefix
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.var = f"{self.prefix}{name}"

    def __get__(self, instance, owner):
        if not hasattr(instance, self.var):
            return None
        return getattr(instance, self.var)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.var} повинен бути строкою")

        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(
                f"Довжина {self.var} повинна бути не менше {self.min_length}"
            )

        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(
                f"Довжина {self.var} повинна бути не більше {self.max_length}"
            )

        if self.var == "username":
            if not re.match(r"^[a-zA-Z0-9_-]{3,25}$", value):
                raise ValueError(
                    f"{self.var} може містити цифри, букви, _ або -, але не починатись з цифри, _ або -"
                )

        if self.var == "password":
            if not re.match(r"^[a-zA-Z0-9_-@#$%^&*()!]+$", value):
                raise ValueError(
                    f"{self.var} може містити цифри, букви, _, -, @#$%^&*()!, але не починатись з цифри, _ або -"
                )

        if self.var == "email":
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
                raise ValueError(
                    f"{self.var} повинен відповідати формату електронної почти"
                )

        setattr(instance, self.var, value)


class User:
    username = Descriptor("username", min_length=3, max_length=25)
    first_name = Descriptor("first_name")
    last_name = Descriptor("last_name")
    email = Descriptor("email")
    password = Descriptor("password")


def t_user():
    user = User()

    user.username = "test_user"
    user.first_name = "John"
    user.last_name = "Doe"
    user.email = "johndoe@example.com"
    user.password = "password123"

    # Define the variable user2
    user2 = User()

    # Print the value of user2.email before the assignment
    print(user2.email)

    # Try to assign the same email to user2 as user
    with pytest.raises(ValueError):
        user2.email = user.email

    # Print the value of user2.email after the assignment
    print(user2.email)

    # Fail the test if user2.email is not None
    if user2.email is not None:
        pytest.fail("user2.email should be None")
