class Person:
    person_id = 1
    def __init__(self, name):
        self.name = name
        self.id = self.person_id
        self.person_id += 1
        self.messages = []

    def text(self, message: str):
        self.messages.append(message)

