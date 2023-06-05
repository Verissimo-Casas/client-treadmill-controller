import socketio

# Cria uma instância do cliente SocketIO
sio = socketio.Client()

@sio.event
def connect():
    print('Conectado ao servidor')

@sio.event
def disconnect():
    print('Desconectado do servidor')

# Função para lidar com o evento de controle do motor recebido do servidor
@sio.event
def controle_motor(comando):
    if comando == 'ligar':
        # Lógica para ligar o motor DC
        print('Motor ligado')
    elif comando == 'desligar':
        # Lógica para desligar o motor DC
        print('Motor desligado')

# Conecta ao servidor
sio.connect('http://localhost:3000')

# Espera por eventos indefinidamente
sio.wait()
