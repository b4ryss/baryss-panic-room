import socket
import threading
import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = ''

def receive():
    global username
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            elif message.startswith('USERNAME_CHANGED '):
                username = message.split(' ')[1]
                print(f'Your username has been changed to {username}')
            elif message.startswith('Username is already taken.'):
                print(message)
                username = input('Please enter a different username: ')
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occurred.')
            client.close()
            break

def main():
    global username
    connected = False  # Bağlantı kontrolü yeri
    username = input('Welcome! Enter your username: ')
    while True:
        command = input('')
        if command.startswith('connect '):
            ip_port = command.split(' ')[1].split(':')
            client.connect((ip_port[0], int(ip_port[1])))
            thread = threading.Thread(target=receive)
            thread.start()
            connected = True
        elif command.startswith('change-username '):
            if not connected:
                print("You must be connected to change your username.")
            elif len(command.split(' ')) < 2:
                print("Invalid usage. Please use 'change-username <new-username>'.")
            else:
                new_username = command.split(' ')[1]
                client.send(f'change-username {new_username}'.encode('utf-8'))
        elif command.startswith('msg '):
            if not connected: 
                print("You must be connected to send messages.")
            else:
                msg_content = command[4:]
                client.send(f'msg {msg_content}'.encode('utf-8'))
                print(f'[{datetime.datetime.now():%d-%m-%Y %H:%M}] {username}: {msg_content}')
        elif command == 'disconnect':
            if not connected: 
                print("You are not connected to any server.")
            else:
                client.close()
                connected = False
                break
        elif command == 'help':
            print('Available commands: connect <ip:port>, change-username <new-username>, msg <message>, disconnect, usercount')
        elif command.startswith('ban '):
            if not connected: 
                print("You must be connected to use the ban command.")
            else:
                target_user = command.split(' ')[1]
                client.send(f'ban {target_user}'.encode('utf-8'))
        elif command.startswith('kick '):
            if not connected: 
                print("You must be connected to use the kick command.")
            else:
                target_user = command.split(' ')[1]
                client.send(f'kick {target_user}'.encode('utf-8'))
        else:
            print("Invalid command. Use 'help' to see available commands.")

if __name__ == "__main__":
    main()
