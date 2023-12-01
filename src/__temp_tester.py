from controller.controlador_principal import login


controlador = login('emcuef', 'hola')
print(controlador.user.__dict__)