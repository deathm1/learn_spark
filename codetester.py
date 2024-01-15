import socket


def send_message(message):
    host = "127.0.0.1"  # Use the same host as your server
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        client_socket.sendall(message.encode("utf-8"))
    finally:
        client_socket.close()


message_to_send = "Hello, server! This is a test message."
send_message(message_to_send)
