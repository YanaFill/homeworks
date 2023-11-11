import re

class Descriptor:

    def __init__(self, name, prefix, min_length, max_length):
        self.name = name
        self.var = prefix + name

    def __get__(self, instance, owner):
        if not hasattr(instance, self.var):
            return None
        return getattr(instance, self.var)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Значення атрибуту має бути типом str")
        if not re.match(r"^[a-zA-Z0-9_-]+$", value):
            raise ValueError("Значення атрибуту має містити тільки букви, цифри, символ підкреслення або мінус")
        if len(value) < self.min_length or len(value) > self.max_length:
            raise ValueError("Довжина значення атрибуту має бути в межах від {} до {}".format(self.min_length, self.max_length))
        setattr(instance, self.var, value)

    def __delete__(self, instance):
        delattr(instance, self.var)

class User:

    username = Descriptor("username", "user_", 3, 20)
    first_name = Descriptor("first_name", "first_", 1, 20)
    last_name = Descriptor("last_name", "last_", 1, 20)
    email = Descriptor("email", "email_", 6, 254)
    password = Descriptor("password", "password_", 6, 254)

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "User(username={}, first_name={}, last_name={}, email={}, password={})".format(
            self.username, self.first_name, self.last_name, self.email, self.password
        )

class User:

    @staticmethod
    def _generate_unique_email(email):
        if not hasattr(User, "_email_cache"):
            User._email_cache = {}
        if email in User._email_cache:
            return User._generate_unique_email(email + "_1")
        User._email_cache[email] = True
        return email

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = self._generate_unique_email(email)
        self.password = password

user = User('Yana Fil', 'Yana', 'Fil', 'yana2004rt@gmail.com', 'qwerty1234')
print(user.username)
print(user.first_name)
print(user.last_name)
print(user.email)
print(user.password)


