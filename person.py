class Person:
    def __init__(self, name):
        self.name = name
        self.last_message = ""

    def text(self, message: str):
        self.last_message = message

    def get_last_message(self):
        return self.last_message

