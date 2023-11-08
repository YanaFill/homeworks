# permissions = ["user", "admin"]
# def required(permission):
#     def decorate(func):
#         def wrapper(*args, **kwargs):
#             if permission in permissions:
#                 func(*args, **kwargs)
#             else:
#                 raise ValueError(f"Нема доступу для користувача {permission}")
#         return wrapper()
#     return decorate()
#
# @required("user")
# def data():
#     print("secret data")
#
# data()



permissions = ["user", "admin"]


class LoginRequired:

    def __init__(self, permission):
        self.permission = permission

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.permission in permissions:
                func(*args, **kwargs)
            else:
                raise ValueError(f"Нема доступу для користувача {self.permission}")
        return wrapper


@LoginRequired("user")
def data():
    print("secret data")


data()
