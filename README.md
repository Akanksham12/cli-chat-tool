# **Chat Room Project Readme**  
This project consists of a simple chat room application implemented in Python using socket programming. The project is divided into two main scripts: server_side.py and client_side.py. The purpose of this chat room is to allow multiple clients to connect to a server and communicate with each other using text messages.

## **Files in the Project**  
server_side.py: This script represents the server-side of the chat room. It handles client connections, message broadcasting, and client disconnections. The server can listen on multiple host-port combinations as specified in the hosts_port.csv file.  

mclient_side.py: This script represents the client-side of the chat room. It allows a user to select a server to connect to from the available options listed in the hosts_port.csv file. The user can then choose a nickname and engage in real-time text-based communication with other clients.  

hosts_port.csv: This CSV file contains a list of available server hosts and ports. The client script uses this file to display the available servers for the user to choose from.  

## **How to Run the Project**  
Running the Server (server_side.py):

Open a terminal.  
Ensure you have Python installed.  
Run the script using the command:  
  ```bash
  python server_side.py.  
```
Running the Client (mclient_side.py):

Open a separate terminal.  
Ensure you have Python installed.  
Run the script using the command:  
```bash  
     python mclient_side.py.  
```
Follow the on-screen prompts to choose a server, provide a nickname, and start chatting.  

## **Usage Instructions**  
Server-Side (server_side.py):

The server script listens for incoming connections from clients.  
It can handle multiple clients concurrently.  
The hosts_port.csv file defines the host and port combinations on which the server listens.  
Clients can connect to these host-port combinations to join the chat room.  
Once clients connect, they can exchange messages with other clients in the chat room.  

Client-Side (mclient_side.py):

The client script allows users to choose a server to connect to from the available options.  
Users must also provide a nickname that will identify them in the chat room.  
After connecting, clients can send and receive messages in the chat room.  
The client script uses threads to simultaneously listen for incoming messages and send user messages.  

## **Important Notes**  
The provided scripts offer basic functionality and may not cover all possible edge cases or security measures.  
This project is meant for educational purposes and may require further refinement for production use.  

## **Dependencies**  
Python 3.x  
pandas (for reading the hosts_port.csv file)  