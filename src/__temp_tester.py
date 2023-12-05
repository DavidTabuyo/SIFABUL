from controller.controlador_principal import login


controlador = login('dtabum00', 'hola')
print(controlador.get_notificaciones())