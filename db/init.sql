CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    salt BLOB NOT NULL,
    hash BLOB NOT NULL
);

CREATE TABLE admins (
    admin_id TEXT,
    PRIMARY KEY (admin_id),
    FOREIGN KEY (admin_id) REFERENCES users(user_id)
);

CREATE TABLE workers (
    worker_id TEXT,
    admin_id TEXT NOT NULL,
    PRIMARY KEY (worker_id),
    FOREIGN KEY (worker_id) REFERENCES users(user_id),
    FOREIGN KEY (admin_id) REFERENCES admins(admin_id)
);



CREATE TABLE notifications (
    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    datetime DATETIME NOT NULL
);

CREATE TABLE workers_notifications (
    worker_id TEXT,
    notification_id INTEGER,
    seen DATETIME,
    PRIMARY KEY (worker_id, notification_id),
    FOREIGN KEY (worker_id) REFERENCES workers(worker_id),
    FOREIGN KEY (notification_id) REFERENCES notifications(notification_id)
);



CREATE TABLE checks (
    worker_id TEXT,
    date DATE,
    time TIME,
    is_entry INTEGER,
    PRIMARY KEY (worker_id, date, time),
    FOREIGN KEY (worker_id) REFERENCES workers(worker_id)
);

CREATE TABLE weeks (
    worker_id TEXT,
    monday DATE,
    total INTEGER NOT NULL,
    PRIMARY KEY (worker_id, monday),
    FOREIGN KEY (worker_id) REFERENCES workers(worker_id)
);