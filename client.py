from lib_chat import Client

def main():
    HOST = '127.0.0.1'
    PORT = 14532
    username = input("Digite seu nome de usuário: ")
    client = Client(HOST, PORT, username)
    client.connect()

    try:
        while True:
            message = input("")
            if message != "sair":
                client.send_message(f"{message}")
            else:
                break
    except KeyboardInterrupt:
        print("Encerrando conexão...")
        client.stop()



if __name__ == "__main__":
    main()

