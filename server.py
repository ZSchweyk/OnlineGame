import socket
from _thread import *
import sys
from server_ip import ip
from person import Person
import pickle

server = ip
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((server, port))
except socket.error as e:
    print("Socket error")
    print(e)

s.listen(2)
print("Waiting for a connection, Server Started")

people = [Person("A"), Person("B")]

def threaded_client(conn, person):
    conn.send(pickle.dumps(people[person]))
    reply = ""
    while True:
        try:
            data = pickle.loads((conn.recv(2048)))
            people[person] = data

            if not data:
                print("Disconnected")
                break
            else:
                if person == 1:
                    reply = people[0]
                else:
                    reply = people[1]

                print(f"Received: {data}")
                print(f"Sending: {reply}")

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


current_person = 0
while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")

    start_new_thread(threaded_client, (conn, current_person))
    current_person += 1
