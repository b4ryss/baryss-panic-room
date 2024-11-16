import socket
import threading
import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = {}
admins = []

def broadcast(message, exclude_client=None):
    for client in clients:
        if client != exclude_client:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                del clients[client]

def handle_client(client):
    try:
        while True:
            message = client.recv(1024).decode('utf-8')
            username = clients[client]
            if message.startswith('msg '):
                formatted_message = f'[{datetime.datetime.now():%d-%m-%Y %H:%M}] {username}: {message[4:]}'
                print(formatted_message)  # Sunucuya mesajı yazdırmak için
                broadcast(formatted_message, client)
            elif message.startswith('kick ') and username in admins:
                target_user = message.split(' ')[1]
                target_client = next((c for c, u in clients.items() if u == target_user), None)
                if target_client:
                    target_client.send('You have been kicked from the server.'.encode('utf-8'))
                    target_client.close()
                    if target_client in clients:
                        del clients[target_client]
                    broadcast(f'{target_user} has been kicked by admin.')
            elif message.startswith('ban ') and username in admins:
                target_user = message.split(' ')[1]
                target_client = next((c for c, u in clients.items() if u == target_user), None)
                if target_client:
                    target_client.send('You have been banned from the server.'.encode('utf-8'))
                    target_client.close()
                    if target_client in clients:
                        del clients[target_client]
                    broadcast(f'{target_user} has been banned by admin.')
            elif message.startswith('change-username '):
                new_username = message.split(' ')[1]
                if new_username in clients.values():
                    client.send(f'Username {new_username} is already taken.'.encode('utf-8'))
                else:
                    old_username = username
                    clients[client] = new_username
                    broadcast(f'{old_username} has changed username to {new_username}')
                    client.send(f'USERNAME_CHANGED {new_username}'.encode('utf-8'))
            else:
                client.send('Unknown command. Use help to see available commands.'.encode('utf-8'))
    except:
        if client in clients:
            username = clients[client]
            client.close()
            del clients[client]
            broadcast(f'{username} has left the chat.')
        else:
            client.close()

def start():
    server.listen()
    print('Server is listening...')
    while True:
        client, address = server.accept()
        client.send('USERNAME'.encode('utf-8'))
        while True:
            username = client.recv(1024).decode('utf-8')
            if username in clients.values():
                client.send('Username is already taken. Please choose a different username.'.encode('utf-8'))
            else:
                clients[client] = username
                break
        broadcast(f'{username} has joined the chat.')
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

def handle_input():
    while True:
        command = input()
        if command.startswith('create '):
            ip_port = command.split(' ')[1].split(':')
            server.bind((ip_port[0], int(ip_port[1])))
            start_thread = threading.Thread(target=start)
            start_thread.start()
        elif command == 'close':
            server.close()
            break
        elif command.startswith('msg '):
            broadcast(f'SERVER: {command[4:]}')
        elif command.startswith('admin '):
            username = command.split(' ')[1]
            if username in clients.values():
                admins.append(username)
                print(f'{username} is now an admin.')
                broadcast(f'{username} has been granted admin privileges.')
            else:
                print(f'User {username} not found.')
        elif command.startswith('kick '):
            username = command.split(' ')[1]
            target_client = next((c for c, u in clients.items() if u == username), None)
            if target_client:
                target_client.send('You have been kicked from the server.'.encode('utf-8'))
                target_client.close()
                if target_client in clients:
                    del clients[target_client]
                broadcast(f'{username} has been kicked by admin.')
            else:
                print(f'User {username} not found.')
        elif command.startswith('ban '):
            username = command.split(' ')[1]
            target_client = next((c for c, u in clients.items() if u == username), None)
            if target_client:
                target_client.send('You have been banned from the server.'.encode('utf-8'))
                target_client.close()
                if target_client in clients:
                    del clients[target_client]
                broadcast(f'{username} has been banned by admin.')
            else:
                print(f'User {username} not found.')
        else:
            print('Unknown command. Use help to see available commands.')

def main():
    print('Commands: help, create <ip:port>, close, msg <message>, admin <username>, kick <username>, ban <username>')
    handle_input_thread = threading.Thread(target=handle_input)
    handle_input_thread.start()

if __name__ == "__main__":
    main()
