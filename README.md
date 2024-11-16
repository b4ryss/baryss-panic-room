# b4ryss' Panic Room

This is a simple terminal-based chat application implemented in Python. It consists of a server (`Server.py`) and a client (`Client.py`). Users can connect to the server, send messages, and perform administrative tasks if they have the appropriate permissions.

There may still be a few problems when using commands in the application, but there are no problems that will make it difficult to use, but do not worry, the bugs will be fixed one by one in the next updates. If you encounter a bug or have suggestions, please contact me.

## Features

- **Messaging**: Send and receive messages in real-time.
- **Username Management**: Change your username before or after connecting.
- **Administration**: Admin users can kick or ban users.
- **Clear Screen**: Clear the terminal screen.
- **User Notifications**: Users are notified when someone joins or leaves the chat.

## Installation

### Requirements

- Python 3.5 or higher

### Setup

1. **Clone the repository**:
    ```bash
    git clone [https://github.com/b4ryss/baryss-panic-room.git]
    cd baryss-panic-room
    ```

2. **Run the server**:
    ```bash
    python3 Server.py
    ```

3. **Run the client**:
    ```bash
    python3 Client.py
    ```

## Usage

### Server Commands

- `help`: Display available commands.
- `create <ip:port>`: Start the server on the specified IP and port.
- `close`: Shut down the server.
- `msg <message>`: Send a message from the server to all clients.
- `admin <username>`: Grant admin privileges to a user.
- `kick <username>`: Remove a user from the server.
- `ban <username>`: Ban a user from the server.

### Client Commands

- `connect <ip:port>`: Connect to the server at the specified IP and port.
- `change-username <new-username>`: Change your username.
- `msg <message>`: Send a message to the chat.
- `disconnect`: Disconnect from the server.
- `clear`: Clear the terminal screen.
- `help`: Display available commands.

## How to Use

### Connecting to the Server

1. **Start the server**:
    - Open a terminal and navigate to the directory containing `Server.py`.
    - Run `python3 Server.py`.
    - Use the `create <ip:port>` command to start the server. For example:
        ```bash
        create 0.0.0.0:5000
        ```

2. **Connect a client**:
    - Open a terminal and navigate to the directory containing `Client.py`.
    - Run `python3 Client.py`.
    - Enter your username when prompted.
    - Use the `connect <ip:port>` command to connect to the server. For example:
        ```bash
        connect 0.0.0.0:5000
        ```

### Changing Username

You can change your username before connecting to the server using the `change-username <new-username>` command but there are still a few problems with this command, so I recommend that you change the username by restarting the client.

### Sending Messages

To send a message to the chat, use the `msg` command followed by your message:

```bash
msg Hello, everyone!
```


### Disconnecting

To disconnect from the server, use the `disconnect` command:

```bash
disconnect
```

### Clearing the Screen

To clear the terminal screen, use the `clear` command:

```bash
clear
```

### Network Configuration for External Access

#### Port Forwarding

If you want clients to connect from outside your local network, you need to set up port forwarding on your router. Forward the port you specified when creating the server (e.g., `5000`) to the local IP address of the machine running the server.

#### How to Set Up Port Forwarding

Port forwarding allows external devices to access services on your local network. Here's a step-by-step guide on how to set it up:

##### 1. Access Your Router's Interface

1. Open a web browser and enter your router's IP address into the address bar (commonly `192.168.1.1` or `192.168.0.1`).
2. Log in with your router's username and password. This information is usually found on the router itself or in its manual.

##### 2. Navigate to Port Forwarding Settings

1. Once logged in, locate the "Port Forwarding" or "Virtual Server" settings. This is usually found under the "Advanced" or "Firewall" section.
2. Click on "Port Forwarding" or "Add New" to create a new rule.

##### 3. Add a New Port Forwarding Rule

1. Enter the following details:
    - **Service Name**: A descriptive name for the service (e.g., "Chat Server").
    - **Port Range**: The port number you want to open (e.g., `5000`).
    - **Local IP**: The local IP address of the device running the server (e.g., `192.168.1.100`).
    - **Protocol**: Select TCP, UDP, or both.
    - **Local Port**: The same port number (e.g., `5000`).

##### 4. Save the Settings and Restart Your Router

1. Save the new port forwarding rule.
2. Restart your router to apply the changes.

##### 5. Setup Server

For the best experience, set up the server as 
```bash 
create 0.0.0.0:port-of-your-choice.
```

##### 6. Use Your Public IP Address

1. For external users to connect, they will need your public IP address instead of `0.0.0.0`.
2. You can find your public IP address using a service like [whatismyipaddress.com](https://whatismyipaddress.com/).

Following these steps will enable port forwarding and allow external devices to access services on your local network. If you have any other questions or need further assistance, feel free to ask! 😊


#### Firewall Configuration

Ensure that your firewall allows traffic on the port you're using for the chat server.

#### Public IP Address

Clients connecting from outside your local network need to use your public IP address instead of `0.0.0.0`.

You can find your public IP address using a service like [whatismyipaddress.com](https://whatismyipaddress.com/).

### Contribution

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.


