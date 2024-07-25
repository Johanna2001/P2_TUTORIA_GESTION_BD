USE MASTER
GO

USE Kinder_Parcial2

GO

--(1) TABLA MENU
create table MENU(
IdMenu int primary key identity(1,1),
Nombre varchar(60),
Icono varchar(60),
Activo bit default 1,
FechaRegistro datetime default getdate()
)

GO

--(2) TABLA SUBMENU
create table SUBMENU(
IdSubMenu int primary key identity(1,1),
IdMenu int references MENU(IdMenu),
Nombre varchar(60),
NombreFormulario varchar(60),
Accion varchar(50),
Activo bit default 1,
FechaRegistro datetime default getdate()
)


GO

--(3) TABLA ROL
create table ROL(
IdRol int primary key identity(1,1),
Descripcion varchar(60),
Activo bit default 1,
FechaRegistro datetime default getdate()
)

GO

--(4) TABLA PERMISOS
create table PERMISOS(
IdPermisos int primary key identity(1,1),
IdRol int references ROL(IdRol),
IdSubMenu int references SUBMENU(IdSubMenu),
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go
--(5) TABLA USUARIO
create table USUARIO(
IdUsuario int primary key identity(1,1),
Nombres varchar(100),
Apellidos varchar(100),
IdRol int references ROL(IdRol),
LoginUsuario varchar(50),
LoginClave varchar(50),
DescripcionReferencia varchar(50),
IdReferencia int,
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go
--(6) TABLA NINIO
create table NINIO(
IdNinio int primary key identity(1,1),
ValorCodigo int,
Codigo varchar(50),
Nombres varchar(100),
Apellidos varchar(100),
DocumentoIdentidad varchar(100),
FechaNacimiento date,
Sexo varchar(50),
Ciudad varchar(100),
Direccion varchar(100),
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go
--(7) TABLA CUIDADOR
create table CUIDADOR(
IdCuidador int primary key identity(1,1),
ValorCodigo int,
Codigo varchar(50),
DocumentoIdentidad varchar(100),
Nombres varchar(100),
Apellidos varchar(100),
FechaNacimiento date,
Sexo varchar(50),
GradoEstudio varchar(100),
Ciudad varchar(100),
Direccion varchar(100),
Email varchar(50),
NumeroTelefono varchar(50),
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go
--(8) TABLA TUTOR
create table TUTOR(
IdTutor int primary key identity(1,1),
TipoRelacion varchar(50),
Nombres varchar(100),
Apellidos varchar(100),
DocumentoIdentidad varchar(100),
FechaNacimiento date,
Sexo varchar(50),
EstadoCivil varchar(50),
Ciudad varchar(100),
Direccion varchar(100),
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go
--(9) TABLA PERIODO
create table PERIODO(
IdPeriodo int primary key identity(1,1),
Descripcion varchar(50),
FechaInicio date,
FechaFin Date,
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go
--(10) TABLA PROGRAMA_SECCION
create table PROGRAMA_SECCION(
IdProgramaSeccion int primary key identity(1,1),
DescripcionCurso varchar(100),
DescripcionSeccion varchar(100),
Activo bit default 1,
FechaRegistro datetime default getdate()
)

go
--(11) TABLA CURSO
create table CURSO(
IdCurso int primary key identity(1,1),
Descripcion varchar(100),
Activo bit default 1,
FechaRegistro datetime default getdate()
)

go
--(12) TABLA NIVEL
create table NIVEL(
IdNivel int primary key identity(1,1),
IdPeriodo int references PERIODO(IdPeriodo),
DescripcionNivel varchar(100),
DescripcionTurno varchar(100),
HoraInicio time,
HoraFin time,
Activo bit default 1,
FechaRegistro datetime default getdate()
)

--(13) TABLA NIVEL_DETALLE
create table NIVEL_DETALLE(
IdNivelDetalle int primary key identity(1,1),
IdNivel int references NIVEL(IdNivel),
IdProgramaSeccion int references PROGRAMA_SECCION(IdProgramaSeccion),
TotalVacantes int,
VacantesDisponibles int,
VacantesOcupadas int,
Activo bit default 1,
FechaRegistro datetime default getdate()
)

go

--(14) TABLA NIVEL_DETALLE_CURSO
create table NIVEL_DETALLE_CURSO(
IdNivelDetalleCurso int primary key identity(1,1),
IdNivelDetalle int references NIVEL_DETALLE(IdNivelDetalle),
IdCurso int references CURSO(IdCurso),
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go

--(15) TABLA HORARIO
create table HORARIO(
IdHorario int primary key identity(1,1),
IdNivelDetalleCurso int references NIVEL_DETALLE_CURSO(IdNivelDetalleCurso),
DiaSemana varchar(50),
HoraInicio time,
HoraFin time,
Activo bit default 1,
FechaRegistro datetime default getdate()
)

go

--(16) TABLA CUIDADOR_NIVELDETALLE_CURSO
create table CUIDADOR_NIVELDETALLE_CURSO(
IdCuidadorNivelDetalleCurso int primary key identity(1,1),
IdNivelDetalleCurso int references NIVEL_DETALLE_CURSO(IdNivelDetalleCurso),
IdCuidador int references CUIDADOR(IdCuidador),
Activo bit default 1,
FechaRegistro datetime default getdate()
)

go

go

--(17) TABLA CURRICULA
create table CURRICULA(
IdCurricula int primary key identity(1,1),
IdCuidadorNivelDetalleCurso int references CUIDADOR_NIVELDETALLE_CURSO(IdCuidadorNivelDetalleCurso),
Descripcion varchar(100),
Activo bit default 1,
FechaRegistro datetime default getdate()
)
go

--(18) TABLA CALIFICACION
create table CALIFICACION(
IdCalificacion int primary key identity(1,1),
IdCurricula int references CURRICULA(IdCurricula),
IdNinio int references NINIO(IdNinio),
Nota float,
Activo bit default 1,
FechaRegistro datetime default getdate()
)

go

--(19) TABLA MATRICULA
create table MATRICULA(
IdMatricula int primary key identity(1,1),
ValorCodigo int,
Codigo varchar(50),
Situacion varchar(50),
IdNinio int references NINIO(IdNinio),
IdNivelDetalle int references NIVEL_DETALLE(IdNivelDetalle),
IdTutor int references TUTOR(IdTutor),
InstitucionProcedencia varchar(50),
EsRepitente bit,
Activo bit default 1,
FechaRegistro datetime default getdate()
)

--(20) TABLA ALERGIA
create table ALERGIA(
IdAlergia int primary key identity(1,1),
IdNinio int references NINIO(IdNinio),
NombreAlergias varchar(20),
DescripcionAlergias varchar(20),
MedicamentoAlergias varchar(20),
Doctor_Tratante varchar(20),
numeroDoctor int,
Activo bit default 1,
FechaRegistro datetime default getdate()
)


