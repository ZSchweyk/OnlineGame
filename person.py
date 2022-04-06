class Person:
    def __init__(self, name):
        self.name = name
        self.messages = ["No Message"]

    def text(self, message: str):
        self.messages.append(message)

    def get_last_message(self):
        return f"{self.name}: {self.messages[-1]}"

