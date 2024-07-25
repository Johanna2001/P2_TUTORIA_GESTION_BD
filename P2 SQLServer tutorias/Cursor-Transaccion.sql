BEGIN TRANSACTION;

BEGIN TRY
    -- Variables de entrada (estas deberían venir de algún procedimiento almacenado o parámetro)
    DECLARE @IdNinio INT = 1; -- ID del niño a matricular
    DECLARE @IdNivelDetalle INT = 1; -- ID del nivel detalle seleccionado
    DECLARE @IdTutor INT = 1; -- ID del tutor asignado
    DECLARE @Situacion VARCHAR(50) = 'Nueva';
    DECLARE @InstitucionProcedencia VARCHAR(50) = 'Ninguna';
    DECLARE @EsRepitente BIT = 0;

    -- Variables para manejo del cursor
    DECLARE @TotalVacantes INT;
    DECLARE @VacantesDisponibles INT;
    DECLARE @VacantesOcupadas INT;
    
    -- Obtener las vacantes del nivel detalle
    SELECT @TotalVacantes = TotalVacantes,
           @VacantesDisponibles = VacantesDisponibles,
           @VacantesOcupadas = VacantesOcupadas
    FROM NIVEL_DETALLE
    WHERE IdNivelDetalle = @IdNivelDetalle;

    -- Verificar si hay vacantes disponibles
    IF @VacantesDisponibles > 0
    BEGIN
        -- Insertar la matrícula del niño
        INSERT INTO MATRICULA (ValorCodigo, Codigo, Situacion, IdNinio, IdNivelDetalle, IdTutor, InstitucionProcedencia, EsRepitente, Activo, FechaRegistro)
        VALUES ((SELECT ISNULL(MAX(ValorCodigo), 0) + 1 FROM MATRICULA), 
                CONCAT('MAT', (SELECT ISNULL(MAX(ValorCodigo), 0) + 1 FROM MATRICULA)),
                @Situacion, @IdNinio, @IdNivelDetalle, @IdTutor, @InstitucionProcedencia, @EsRepitente, 1, GETDATE());

        -- Actualizar las vacantes en NIVEL_DETALLE
        UPDATE NIVEL_DETALLE
        SET VacantesDisponibles = VacantesDisponibles - 1,
            VacantesOcupadas = VacantesOcupadas + 1
        WHERE IdNivelDetalle = @IdNivelDetalle;

        COMMIT TRANSACTION;
    END
    ELSE
    BEGIN
        -- Si no hay vacantes disponibles, lanzar un error
        THROW 51000, 'No hay vacantes disponibles en el nivel seleccionado.', 1;
    END
END TRY
BEGIN CATCH
    -- Manejar errores y realizar rollback en caso de fallo
    ROLLBACK TRANSACTION;
    DECLARE @ErrorMessage NVARCHAR(4000);
    DECLARE @ErrorSeverity INT;
    DECLARE @ErrorState INT;

    SELECT @ErrorMessage = ERROR_MESSAGE(),
           @ErrorSeverity = ERROR_SEVERITY(),
           @ErrorState = ERROR_STATE();

    RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
END CATCH;
