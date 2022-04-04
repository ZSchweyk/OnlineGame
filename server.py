import socket
from _thread import *
import sys

server = "10.107.100.24"
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


def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data



            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print(f"Received: {data}")
                print(f"Sending: {reply}")

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
