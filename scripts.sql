
CREATE TABLE paciente(
	rut VARCHAR(12) NOT NULL PRIMARY KEY,
	nombre VARCHAR(80),
	fecha_nacimiento DATE
);

CREATE TABLE vacuna(
	id_vacuna INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nombre_enfermedad VARCHAR(80)
);

CREATE TABLE recibe(
	rut VARCHAR(12),
	id_vacuna INT,
	FOREIGN KEY(rut) REFERENCES paciente(rut),
	FOREIGN KEY(id_vacuna) REFERENCES vacuna(id_vacuna)
);

