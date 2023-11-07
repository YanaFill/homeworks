from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onclick(self):
        pass


class WindowsButton(Button):

    def render(self):
        print("Відобразити кнопку в стилі Windows")

    def onclick(self):
        print("Кнопка Windows була натиснута")

class HTMLButton(Button):

    def render(self):
        print("Повернути HTML-код кнопки")

    def onclick(self):
        print("Навісити на кнопку обробник події браузера")

class MacButton(Button):

    def render(self):
        print("Повернути Mac-код кнопки")

    def onclick(self):
        print("Навісити на кнопку обробник події браузера")


class Dialog(ABC):
    def render_dialog(self):
        button = self.createButton()
        button.render()
        button.onclick()

    @abstractmethod
    def createButton(self) -> Button:
        pass


class WindowsDialog(Dialog):

    def createButton(self):
        print("Створено кнопку Windows")
        return WindowsButton()

class WebDialog(Dialog):

    def createButton(self):
        print("Створено кнопку HTML")
        return HTMLButton()

def client_code(creator: Dialog) -> None:
    print("__Start__")
    creator.render_dialog()

class MacDialog(Dialog):

    def createButton(self):
        print("Створено кнопку Mac")
        return MacButton()




if __name__ == "__main__":
    client_code(WindowsDialog())
    client_code(WebDialog())
    client_code(MacDialog())












