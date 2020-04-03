
CREATE TABLE paciente(
	rut VARCHAR(12) NOT NULL PRIMARY KEY,
	nombre VARCHAR(80),
	fecha_nacimiento DATE
);

CREATE TABLE vacuna(
	nombre_enfermedad VARCHAR(80) NOT NULL PRIMARY KEY,
	fecha_registro DATE
);

CREATE TABLE recibe(
	fecha_vacuna DATE,
	rut VARCHAR(12),
	nombre_enfermedad VARCHAR(80),
	FOREIGN KEY(rut) REFERENCES paciente(rut),
	FOREIGN KEY(nombre_enfermedad) REFERENCES vacuna(nombre_enfermedad)
);

INSERT INTO paciente VALUES('11.111.111-1','Ana Mora','1993-01-01');
INSERT INTO paciente VALUES('11.222.222-2','Pablo Santos','1983-02-02');
INSERT INTO paciente VALUES('11.333.333-3','Patricio Estrella','1990-10-06');

INSERT INTO vacuna VALUES('enfermedad1','2010-01-01');
INSERT INTO vacuna VALUES('enfermedad2','2017-01-01');

INSERT INTO recibe VALUES('11.111.111-1','enfermedad1','2020-01-01');
INSERT INTO recibe VALUES('11.111.111-1','enfermedad2','2014-02-03');
INSERT INTO recibe VALUES('11.333.333-3','enfermedad2','2018-04-05');