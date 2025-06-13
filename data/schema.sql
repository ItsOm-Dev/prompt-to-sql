-- schema.sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    signup_date DATE NOT NULL
);

INSERT INTO users (name, email, signup_date) VALUES
('Alice', 'alice@example.com', DATE('now', '-2 days')),
('Bob', 'bob@example.com', DATE('now', '-5 days')),
('Charlie', 'charlie@example.com', DATE('now', '-10 days'));
