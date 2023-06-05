import socketio

# Cria uma instância do servidor SocketIO
sio = socketio.Server()

# Função para lidar com o evento de conexão do cliente
@sio.event
def connect(sid, environ):
    print('Cliente conectado:', sid)
    # Envia o comando 'ligar' para o cliente ao se conectar
    sio.emit('controle_motor', 'ligar', room=sid)

# Função para lidar com o evento de desconexão do cliente
@sio.event
def disconnect(sid):
    print('Cliente desconectado:', sid)

# Cria uma aplicação WSGI para o servidor SocketIO
app = socketio.WSGIApp(sio)

# Executa o servidor na porta 3000
if __name__ == '__main__':
    import eventlet
    eventlet.wsgi.server(eventlet.listen(('', 3000)), app)
