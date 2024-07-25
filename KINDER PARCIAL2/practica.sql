USE MASTER
GO

USE Kinder_Parcial2

GO

SELECT * FROM AUDITORIA
INSERT INTO HORARIO (IdNivelDetalleCurso, DiaSemana, HoraInicio, HoraFin) VALUES (1, 'Lunes', '10:00:00', '12:00:00')

DELETE FROM HORARIO
WHERE IdNivelDetalleCurso = 1
  AND DiaSemana = 'Lunes'
  AND HoraInicio = '10:00:00'
  AND HoraFin = '12:00:00';

SELECT * FROM AUDITORIA



SELECT * FROM NIVEL_DETALLE

SELECT * FROM MATRICULA WHERE IdNinio = 1;
SELECT * FROM NIVEL_DETALLE WHERE IdNivelDetalle = 1;

