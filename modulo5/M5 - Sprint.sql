--Crear base de datos
CREATE DATABASE puedoayudarte;

--Usar la nueva base de datos
USE puedoayudarte;

--Crear un usuario admin para la base de datos y otorgarle todos los privilegios
CREATE USER 'puedoayudarte_admin'@'localhost' IDENTIFIED BY 'lapass';
GRANT ALL PRIVILEGES ON puedoayudarte.* TO 'puedoayudarte_admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

--Crear las tablas
CREATE TABLE usuarios (
id SMALLINT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(40),
apellido VARCHAR(40),
edad TINYINT,
correo_electronico VARCHAR(150),
veces_aplicacion SMALLINT DEFAULT 1,
PRIMARY KEY (id)
);

ALTER TABLE usuarios AUTO_INCREMENT=1;
CREATE TABLE operarios (
id SMALLINT NOT NULL AUTO_INCREMENT,
nombre VARCHAR(40),
apellido VARCHAR(40),
edad TINYINT,
correo_electronico VARCHAR(150),
veces_soporte SMALLINT DEFAULT 1,
PRIMARY KEY (id)
);

ALTER TABLE operarios AUTO_INCREMENT=1;
CREATE TABLE soportes (
operario_id SMALLINT,
usuario_id SMALLINT,
fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
nota TINYINT,
comentario TEXT,
PRIMARY KEY (operario_id, usuario_id, fecha),
FOREIGN KEY (operario_id) REFERENCES operarios (id),
FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);

--Insertar los datos
INSERT INTO usuarios (nombre, apellido, edad, correo_electronico, veces_aplicacion)
VALUES ('Alberto', 'Garcia', 32, 'alberto.garcia@awakelab.cl', 7),
('Steffania', 'Schweikart',25, 'steffania.schweikart@awakelab.cl', 8),
('Jose', 'Martinez', 35, 'jose.martinez@awakelab.cl', 4),
('Balta', 'Fernandez', 37, 'balta.fernandez@awakelab.cl', 2),
('Hugo', 'Gonzalez', 18, 'hugo.gonzalez@awakelab.cl', 1)
;

INSERT INTO operarios (nombre, apellido, edad, correo_electronico, veces_soporte)
VALUES ('Anibal', 'Reinoso', 43, 'anibal.reinoso@awakelab.cl', 145),
('Rodrigo', 'Testa',27, 'rodrigo.testa@awakelab.cl', 124),
('Luis', 'Martinez', 21, 'luis.martinez@awakelab.cl', 41),
('Ivan', 'Hernandez', 19, 'ivan.hernandez@awakelab.cl', 29),
('Jose', 'Rodriguez', 29, 'jose.rodriguez @awakelab.cl', 13)
;

INSERT INTO soportes (operario_id, usuario_id, fecha, nota, comentario)
VALUES (2, 1, '2023-02-01 11:13:47', 7, 'Lorem ipsum etc'),
(3, 4, '2023-02-03 14:23:17', 6, 'Lorem ipsum xD'),
(1, 2, '2023-05-04 12:15:11', 4, 'Lorem ipsum etc'),
(5, 4, '2023-04-02 11:13:47', 5, 'Lorem ipsum etc'),
(1, 5, '2023-05-03 10:09:00', 7, 'Lorem ipsum etc'),
(4, 3, '2023-01-01 00:05:47', 2, 'No mostró mucho interés en atenderme'),
(1, 1, '2023-02-14 15:13:05', 5, '………..'),
(4, 4, '2023-05-17 11:13:47', 7, 'Lorem ipsum etc'),
(3, 3, '2022-12-30 18:36:57', 6, 'Lorem ipsum'),
(5, 5, '2023-03-06 16:15:16', 7, 'Lorem ipsum etc')
;


--Seleccione las 3 operaciones con mejor evaluación.
SELECT * FROM soportes
ORDER BY nota DESC
LIMIT 3;

--Seleccione las 3 operaciones con peor evaluación.
SELECT * FROM soportes
ORDER BY nota ASC
LIMIT 3;

--Seleccione al operario que más soportes ha realizado.
SELECT * FROM operarios
WHERE veces_soporte = (SELECT MAX(veces_soporte) FROM operarios);

--Seleccione al cliente que menos veces ha utilizado la aplicación.
SELECT * FROM usuarios
WHERE veces_aplicacion = (SELECT MIN(veces_aplicacion) FROM usuarios);

--Agregue 10 años a los tres primeros usuarios registrados.
UPDATE usuarios
SET edad = edad + 10
WHERE id IN (SELECT id FROM (SELECT id FROM usuarios ORDER BY id ASC LIMIT 0,3) tmp);

--Renombre todas las columnas ‘correo electrónico’. El nuevo nombre debe ser email.
ALTER TABLE usuarios
RENAME COLUMN correo_electronico TO email;
ALTER TABLE operarios
RENAME COLUMN correo_electronico TO email;

--Seleccione solo los operarios mayores de 20 años.
SELECT * FROM usuarios
WHERE edad > 20;