--Numero de estudiantes con mas de 30 años--
SELECT COUNT(*) FROM estudiantes WHERE edad > 30;

--Estudiantes cuyo color favorito NO es el amarillo--
SELECT * FROM estudiantes WHERE color_preferido != 'amarillo';

--Estudiantes con edad entre 50 y 60--
SELECT * FROM estudiantes WHERE edad BETWEEN 50 AND 60;

--Eliminamos tabla estudiantes--
DROP TABLE estudiantes;

--Estudiantes que no son del 2023-01-10--
SELECT * FROM estudiantes WHERE fecha_nacimiento != '2023-01-10';
