CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    salt TEXT NOT NULL,
    hash TEXT NOT NULL
);

CREATE TABLE becarios (
    becario_id TEXT,
    responsable_id TEXT NOT NULL,
    PRIMARY KEY (becario_id),
    FOREIGN KEY (becario_id) REFERENCES users(user_id)
    FOREIGN KEY (responsable_id) REFERENCES responsables(responsable_id)
);

CREATE TABLE responsables (
    responsable_id TEXT,
    PRIMARY KEY (responsable_id),
    FOREIGN KEY (responsable_id) REFERENCES users(user_id)
);




----------------------------------------------------------------------------

INSERT INTO users (user_id, nombre, salt, hash) VALUES
    ('ogingd00', 'Demi', '98766', 'iou7y6tfgiou8y7gtfhbjnkiu87y6'),
    ('vtunog00', 'Victor', '65293', '87yt6fhgjuiy76tfghuiy87tg'),
    ('dmartm14', 'Dario', '34567', 'ygtfrhdbjjjjjktyfghjbk'),
    ('dtabum00', 'David', '82543', '987y6trfghuiy76thbjnkiuyg'),
    ('emcuef', 'Eva Cuervo', '03785', 'iyjikuyhguyghjtfhbjnuiyg');

INSERT INTO responsables (responsable_id) VALUES
    ('emcuef');

INSERT INTO becarios (becario_id, responsable_id) VALUES
    ('ogingd00', 'emcuef'),
    ('vtunog00', 'emcuef'),
    ('dmartm14', 'emcuef'),
    ('dtabum00', 'emcuef');

