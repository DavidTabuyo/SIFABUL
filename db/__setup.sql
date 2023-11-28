-- CREATE TABLE users (
--     user_id TEXT PRIMARY KEY,
--     nombre TEXT NOT NULL,
--     salt BLOB NOT NULL,
--     hash BLOB NOT NULL
-- );

CREATE TABLE responsables (
    responsable_id TEXT,
    PRIMARY KEY (responsable_id),
    FOREIGN KEY (responsable_id) REFERENCES users(user_id)
);

CREATE TABLE becarios (
    becario_id TEXT,
    responsable_id TEXT NOT NULL,
    PRIMARY KEY (becario_id),
    FOREIGN KEY (becario_id) REFERENCES users(user_id),
    FOREIGN KEY (responsable_id) REFERENCES responsables(responsable_id)
);



CREATE TABLE notificaciones (
    notificacion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_hora DATETIME NOT NULL
);

CREATE TABLE becarios_notificaciones (
    becario_id TEXT,
    notificacion_id INTEGER,
    is_vista INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (becario_id, notificacion_id),
    FOREIGN KEY (becario_id) REFERENCES becarios(becario_id),
    FOREIGN KEY (notificacion_id) REFERENCES notificaciones(notificacion_id)
);



CREATE TABLE fichajes (
    becario_id TEXT,
    fecha DATE,
    hora TIME,
    is_entrada INTEGER,
    PRIMARY KEY (becario_id, fecha, hora),
    FOREIGN KEY (becario_id) REFERENCES becarios(becario_id)
);

CREATE TABLE semanas (
    becario_id TEXT,
    lunes DATE,
    total_semana INTEGER NOT NULL,
    PRIMARY KEY (becario_id, lunes),
    FOREIGN KEY (becario_id) REFERENCES becarios(becario_id)
);






----------------------------------------------------------------------------
INSERT INTO responsables (responsable_id) VALUES
    ('emcuef');

INSERT INTO becarios (becario_id, responsable_id) VALUES
    ('ogingd00', 'emcuef'),
    ('vtunog00', 'emcuef'),
    ('dmartm14', 'emcuef'),
    ('dtabum00', 'emcuef');



INSERT INTO notificaciones (titulo, descripcion, fecha_hora) VALUES
    ('Aula 101', 'Necesito que reinicieis todos los equipos', '2023-11-24 14:31:54'),
    ('Limpiar', 'Limpiad porfavor el teclado y el ratos del aula 217', '2023-11-24 10:03:18'),
    ('Instalar AutoCAD', 'Necesito intaleis autocad en todos los equipos de la 103 para mañana', '2023-11-24 19:15:45');

INSERT INTO becarios_notificaciones (notificacion_id, becario_id) VALUES
    (1, 'dmartm14'), (1, 'dtabum00'), (1, 'ogingd00'),
    (2, 'vtunog00'), (2, 'ogingd00'),
    (3, 'dmartm14'), (3, 'dtabum00'), (3, 'vtunog00'), (3, 'ogingd00');



INSERT INTO fichajes (becario_id, fecha, hora, is_entrada) VALUES
    ('dtabum00', '2023-11-25', '12:29:34', 1),
    ('dtabum00', '2023-11-25', '12:34:56', 0),
    ('vtunog00', '2023-11-26', '12:35:01', 1),
    ('vtunog00', '2023-11-26', '12:33:45', 1);