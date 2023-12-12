INSERT INTO admins (admin_id) VALUES
    ('emcuef');

INSERT INTO workers (worker_id, admin_id) VALUES
    ('ogingd00', 'emcuef'),
    ('vtunog00', 'emcuef'),
    ('dmartm14', 'emcuef'),
    ('dtabum00', 'emcuef');



INSERT INTO notifications (title, description, datetime) VALUES
    ('Aula 101', 'Necesito que reinicieis todos los equipos', '2023-11-24 14:31:54'),
    ('Limpiar', 'Limpiad porfavor el teclado y el ratos del aula 217', '2023-11-24 10:03:18'),
    ('Instalar AutoCAD', 'Necesito intaleis autocad en todos los equipos de la 103 para mañana', '2023-11-24 19:15:45');

INSERT INTO workers_notifications (notification_id, worker_id) VALUES
    (1, 'dmartm14'), (1, 'dtabum00'), (1, 'ogingd00'),
    (2, 'vtunog00'), (2, 'ogingd00'),
    (3, 'dmartm14'), (3, 'dtabum00'), (3, 'vtunog00'), (3, 'ogingd00');