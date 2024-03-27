import socket
import threading

class ClientHandler(threading.Thread):
    def __init__(self, client_socket, client_address, server):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.server = server
        self.username = None

    def run(self):
        try:
            self.username = self.client_socket.recv(1024).decode('utf-8')
            self.server.broadcast_message(f"{self.username} entrou no chat.")
            print(f"Novo usuário {self.username} conectado.")
            while True:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    formatted_message = f"{self.username}: {message}"
                    print(formatted_message)
                    self.server.broadcast_message(formatted_message, exclude=[self.client_socket])
        except ConnectionResetError:
            print(f"Conexão com {self.username} foi redefinida.")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            print(f"Usuário {self.username} desconectou do servidor.")
            self.server.remove_client(self.client_socket)
            self.client_socket.close()

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_handlers = []
        self.is_running = True

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Servidor escutando na porta: {self.port}")
        threading.Thread(target=self.send_server_message, daemon=True).start()

    def accept_client(self):
        if self.is_running:
            try:
                client_socket, client_address = self.server_socket.accept()
                client_handler = ClientHandler(client_socket, client_address, self)
                client_handler.start()
                self.client_handlers.append(client_handler)
            except socket.error as e:
                if self.is_running:  # Se o servidor ainda estiver em execução, logar o erro
                    print(f"Erro ao aceitar cliente: {e}")

    def broadcast_message(self, message, exclude=[]):
        for handler in self.client_handlers:
            if handler.client_socket not in exclude:
                try:
                    handler.client_socket.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Erro ao enviar mensagem: {e}")
                    self.remove_client(handler.client_socket)

    def remove_client(self, client_socket):
        self.client_handlers = [handler for handler in self.client_handlers if handler.client_socket != client_socket]

    def send_server_message(self):
        while self.is_running:
            message = input("")
            if message != "sair":
                self.broadcast_message(f"Servidor: {message}")
            else:             
                self.stop()
                break

    def stop(self):
        if self.is_running:
            print("Desligando o servidor...")
            self.is_running = False
            for handler in self.client_handlers:
                handler.client_socket.close()
                handler.join()  # Aguardar a thread do handler terminar
            self.server_socket.close()
            print("Servidor desligado.")


class Client:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_running = True

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        self.client_socket.send(self.username.encode('utf-8'))
        print("Conectado ao servidor. Você pode começar a enviar mensagens.")
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))

    def receive_messages(self):
        while self.is_running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message.startswith(self.username + ":"):  # Verifica se a mensagem não é do próprio usuário
                    print(message)
            except Exception as e:
                print(f"Erro: {e}")
                print("Conexão encerrada.")
                break

    def stop(self):
        self.is_running = False
        self.client_socket.close()
