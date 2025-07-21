CREATE DATABASE IF NOT EXISTS inventory_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE inventory_app;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    role ENUM('admin', 'operator') NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

INSERT INTO users (username, role, password_hash) VALUES
('operator1', 'operator', '$2b$12$IVBI5plmMcHbC6nJy05Kk.FQD47Xd3QzxOpEYQKqSTdsn.1POeOLe'),
('operator2', 'operator', '$2b$12$uN9cRjMa2pIpPOSmeL/TV.rQ8XjYdnrY0xXQPleBv7M6yays0RYLa');
