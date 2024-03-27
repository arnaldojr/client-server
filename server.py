from lib_chat import Server

def main():
    HOST = '127.0.0.1'
    PORT = 14532

    try:
        server = Server(HOST, PORT)
        server.start()
        while server.is_running:
            server.accept_client() # Aceita novos clientes
    except KeyboardInterrupt:
        print("Encerrando servidor...")
    finally:
        server.stop()


if __name__ == "__main__":
    main()
    
