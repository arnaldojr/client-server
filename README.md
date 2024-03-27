## Chat em Tempo Real com Python

Exemplo simples para demonstrar uma aplicação `Client-Server` por meio de um `chat` usando sockets. Basicamente, consiste em um `servidor` que gerencia as mensagens entre os `clientes` conectados. Cada cliente e servidor podem enviar e receber mensagens.

![](client-server.gif)

link do video no youtube: [https://youtu.be/O9wSH3AHaog](https://youtu.be/O9wSH3AHaog)

## Conceitos Principais de Client-Server

O modelo cliente-servidor é uma arquitetura de rede que segmenta as tarefas entre os provedores de recursos ou serviços, conhecidos como servidores, e os solicitantes de serviços, conhecidos como clientes. Geralmente, os clientes e servidores se comunicam por uma rede de computadores em protocolos de rede específicos.

- `Servidor`: Gerencia o acesso a um recurso ou serviço centralizado em uma rede. Os servidores geralmente têm capacidades de processamento, armazenamento e memória superiores em comparação com os clientes. Eles aguardam e atendem às solicitações dos clientes. Exemplos de servidores incluem servidores web, servidores de e-mail e servidores de banco de dados.

- `Cliente`: Solicita acesso a um recurso ou serviço fornecido por um servidor. Os clientes iniciam as comunicações com os servidores para solicitar serviços. Exemplos de clientes incluem navegadores web, clientes de e-mail e aplicativos de banco de dados.

- `Protocolo de Comunicação`: A comunicação entre clientes e servidores é regida por protocolos de rede que definem as regras e convenções para troca de dados. Alguns dos protocolos de comunicação comuns incluem HTTP (para comunicação na web), FTP (para transferência de arquivos), SMTP (para e-mail) entre outros como TCP/IP RTSP, MQTT.... É importante entender como os protocolos de rede funcionam para facilitar a comunicação entre clientes e servidores.

- `APIs e Serviços Web`: Conhecimento sobre como as APIs (Application Programming Interfaces) e os serviços web permitem a comunicação e a integração entre diferentes sistemas e aplicativos em uma arquitetura cliente-servidor.

## Como Executar

1. Clone o repositório.

```bash
git clone https://github.com/arnaldojr/client-server.git
cd client-server
```

2. Inicie `primeiramente` o servidor:

```bash
python server.py
```

3. Em outro terminal, inicie um ou mais clientes:

```bash
python client.py
```

4. Digite seu nome de usuário e comece a enviar mensagens 😁. Para sair do programa, digite "sair".

