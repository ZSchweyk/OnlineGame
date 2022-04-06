from network import Network
from person import Person




def main():
    run = True
    n = Network()
    person1: Person = n.get_person()
    print(f"You are {person1.name}")

    while run:
        person2: Person = n.send(person1)

        person1.text(input("Enter Message\n"))
        print(f"{person2.name} said: {person2.get_last_message()}")


main()

