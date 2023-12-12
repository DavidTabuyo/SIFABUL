from controller.login_controller import login


controlador = login('dtabum00', 'hola')
checks = controlador.get_today_checks()
print(*(check.get_output() for check in checks))