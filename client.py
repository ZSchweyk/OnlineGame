from network import Network
from person import Person




def main():
    run = True
    n = Network()
    person1: Person = n.get_person()
    print(f"You are {person1.name}")

    while run:
        person2: Person = n.send(person1)

        person1.text(input(""))
        if person1.id == 2:
            while len(person1.messages) == 0:
                pass
            print(f"{person1.messages[-1]}")
        else:
            while len(person2.messages) == 0:
                pass
            print(f"{person2.messages[-1]}")


main()

