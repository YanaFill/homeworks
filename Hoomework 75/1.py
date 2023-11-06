from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message, receiver):
        pass


class EmailService(NotificationService):
    def send_notification(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")


class SmsService(NotificationService):
    def send_notification(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")


class NotificationFactory:
    @staticmethod
    def create_notification_service(method):
        if method == "email":
            return EmailService()
        elif method == "sms":
            return SmsService()
        else:
            raise ValueError(f"Unknown notification method: {method}")


def t_send_notification():
    notification_service = NotificationFactory.create_notification_service("sms")
    notification_service.send_notification("Test SMS", "+380999999999")


# Define a function called test_send_email()
def t_send_email():
    notification_service = NotificationFactory.create_notification_service("email")
    notification_service.send_notification("Test email", "test@example.com")


if __name__ == "__main__":
    # Change the name of the function to test_send_sms()
    t_send_notification()
    t_send_email()
