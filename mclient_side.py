import pandas as pd
import socket
import threading

# Read the "hosts_port.csv" file
df = pd.read_csv('hosts_port.csv')

# Display the available servers
print("\nAvailable Servers:")
for i, row in df.iterrows():
    print(f"{i+1}. Host: {row['hosts']}, Port: {row['ports']}")

# Prompt the user to choose a server
selection = int(input("\nEnter the server number to connect: "))

# Retrieve the host and port of the selected server
server_host = df.loc[selection - 1, 'hosts']
server_port = df.loc[selection - 1, 'ports']

# Prompt the user to choose a nickname
nickname = input("Choose your nickname: ")

# Connect to the selected server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_host, server_port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        try:
            message = '{}: {}'.format(nickname, input(''))
            client.send(message.encode('ascii'))
        except:
            print("An error occurred!")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
