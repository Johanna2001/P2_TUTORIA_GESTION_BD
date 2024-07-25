USE Kinder_Parcial2
GO

-- Insertar datos en la tabla MENU
INSERT INTO MENU (Nombre, Icono) VALUES 
('Menu1', 'Icon1'),
('Menu2', 'Icon2');

-- Insertar datos en la tabla SUBMENU
INSERT INTO SUBMENU (IdMenu, Nombre, NombreFormulario, Accion) VALUES 
(1, 'SubMenu1', 'Formulario1', 'Accion1'),
(2, 'SubMenu2', 'Formulario2', 'Accion2');

-- Insertar datos en la tabla ROL
INSERT INTO ROL (Descripcion) VALUES 
('Rol1'),
('Rol2');

-- Insertar datos en la tabla PERMISOS
INSERT INTO PERMISOS (IdRol, IdSubMenu) VALUES 
(1, 1),
(2, 2);

-- Insertar datos en la tabla USUARIO
INSERT INTO USUARIO (Nombres, Apellidos, IdRol, LoginUsuario, LoginClave, DescripcionReferencia, IdReferencia) VALUES 
('Juan', 'Perez', 1, 'jperez', 'clave123', 'Ref1', 1),
('Ana', 'Gomez', 2, 'agomez', 'clave456', 'Ref2', 2);

-- Insertar datos en la tabla NINIO
INSERT INTO NINIO (ValorCodigo, Codigo, Nombres, Apellidos, DocumentoIdentidad, FechaNacimiento, Sexo, Ciudad, Direccion) VALUES 
(1, 'NINIO1', 'Carlos', 'Lopez', '123456789', '2010-01-01', 'M', 'Ciudad1', 'Direccion1'),
(2, 'NINIO2', 'Maria', 'Garcia', '987654321', '2011-02-02', 'F', 'Ciudad2', 'Direccion2');

-- Insertar datos en la tabla CUIDADOR
INSERT INTO CUIDADOR (ValorCodigo, Codigo, DocumentoIdentidad, Nombres, Apellidos, FechaNacimiento, Sexo, GradoEstudio, Ciudad, Direccion, Email, NumeroTelefono) VALUES 
(1, 'CUIDADOR1', '111111111', 'Pedro', 'Ramirez', '1980-03-03', 'M', 'Secundaria', 'Ciudad1', 'Direccion1', 'pedro@example.com', '1234567890'),
(2, 'CUIDADOR2', '222222222', 'Luisa', 'Martinez', '1985-04-04', 'F', 'Universitario', 'Ciudad2', 'Direccion2', 'luisa@example.com', '0987654321');

-- Insertar datos en la tabla TUTOR
INSERT INTO TUTOR (TipoRelacion, Nombres, Apellidos, DocumentoIdentidad, FechaNacimiento, Sexo, EstadoCivil, Ciudad, Direccion) VALUES 
('Padre', 'Jose', 'Hernandez', '333333333', '1975-05-05', 'M', 'Casado', 'Ciudad1', 'Direccion1'),
('Madre', 'Laura', 'Fernandez', '444444444', '1978-06-06', 'F', 'Soltero', 'Ciudad2', 'Direccion2');

-- Insertar datos en la tabla PERIODO
INSERT INTO PERIODO (Descripcion, FechaInicio, FechaFin) VALUES 
('Periodo 2023', '2023-01-01', '2023-12-31'),
('Periodo 2024', '2024-01-01', '2024-12-31');

-- Insertar datos en la tabla PROGRAMA_SECCION
INSERT INTO PROGRAMA_SECCION (DescripcionCurso, DescripcionSeccion) VALUES 
('Curso1', 'Seccion1'),
('Curso2', 'Seccion2');

-- Insertar datos en la tabla CURSO
INSERT INTO CURSO (Descripcion) VALUES 
('Matemáticas'),
('Lenguaje');

-- Insertar datos en la tabla NIVEL
INSERT INTO NIVEL (IdPeriodo, DescripcionNivel, DescripcionTurno, HoraInicio, HoraFin) VALUES 
(1, 'Primaria', 'Mañana', '08:00:00', '12:00:00'),
(2, 'Secundaria', 'Tarde', '13:00:00', '17:00:00');

-- Insertar datos en la tabla NIVEL_DETALLE
INSERT INTO NIVEL_DETALLE (IdNivel, IdProgramaSeccion, TotalVacantes, VacantesDisponibles, VacantesOcupadas) VALUES 
(1, 1, 30, 10, 20),
(2, 2, 25, 5, 20);

-- Insertar datos en la tabla NIVEL_DETALLE_CURSO
INSERT INTO NIVEL_DETALLE_CURSO (IdNivelDetalle, IdCurso) VALUES 
(1, 1),
(2, 2);

-- Insertar datos en la tabla HORARIO
INSERT INTO HORARIO (IdNivelDetalleCurso, DiaSemana, HoraInicio, HoraFin) VALUES 
(1, 'Lunes', '08:00:00', '10:00:00'),
(2, 'Martes', '10:00:00', '12:00:00');

-- Insertar datos en la tabla CUIDADOR_NIVELDETALLE_CURSO
INSERT INTO CUIDADOR_NIVELDETALLE_CURSO (IdNivelDetalleCurso, IdCuidador) VALUES 
(1, 1),
(2, 2);

-- Insertar datos en la tabla CURRICULA
INSERT INTO CURRICULA (IdCuidadorNivelDetalleCurso, Descripcion) VALUES 
(1, 'Curricula1'),
(2, 'Curricula2');

-- Insertar datos en la tabla CALIFICACION
INSERT INTO CALIFICACION (IdCurricula, IdNinio, Nota) VALUES 
(1, 1, 90.5),
(2, 2, 85.0);

-- Insertar datos en la tabla MATRICULA
INSERT INTO MATRICULA (ValorCodigo, Codigo, Situacion, IdNinio, IdNivelDetalle, IdTutor, InstitucionProcedencia, EsRepitente) VALUES 
(1, 'MAT1', 'Activa', 1, 1, 1, 'Instituto1', 0),
(2, 'MAT2', 'Activa', 2, 2, 2, 'Instituto2', 1);

-- Insertar datos en la tabla ALERGIA
INSERT INTO ALERGIA (IdNinio, NombreAlergias, DescripcionAlergias, MedicamentoAlergias, Doctor_Tratante, numeroDoctor) VALUES 
(1, 'Polen', 'Alergia al polen', 'Antihistamínico', 'Dr. Smith', 123456),
(2, 'Lactosa', 'Intolerancia a la lactosa', 'Enzimas', 'Dr. Jones', 654321);

select *from HORARIO

