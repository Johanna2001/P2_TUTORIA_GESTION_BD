import pyodbc
import tkinter as tk
from tkinter import messagebox

def automatizar_matricula(id_ninio, id_nivel_detalle, id_tutor, situacion, institucion_procedencia, es_repitente):
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=SANDY-CQ11\SJCQ11;'
        'DATABASE=Kinder_Parcial2;'
        'UID=SANDY-CQ11\1116;'
        'PWD=Sandy1116;'
        'Trusted_Connection=yes'
    )
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    try:
        cursor.execute("""
        BEGIN TRANSACTION;

        BEGIN TRY
            DECLARE @IdNinio INT = ?;
            DECLARE @IdNivelDetalle INT = ?;
            DECLARE @IdTutor INT = ?;
            DECLARE @Situacion VARCHAR(50) = ?;
            DECLARE @InstitucionProcedencia VARCHAR(50) = ?;
            DECLARE @EsRepitente BIT = ?;

            DECLARE @TotalVacantes INT;
            DECLARE @VacantesDisponibles INT;
            DECLARE @VacantesOcupadas INT;

            SELECT @TotalVacantes = TotalVacantes,
                   @VacantesDisponibles = VacantesDisponibles,
                   @VacantesOcupadas = VacantesOcupadas
            FROM NIVEL_DETALLE
            WHERE IdNivelDetalle = @IdNivelDetalle;

            IF @VacantesDisponibles > 0
            BEGIN
                INSERT INTO MATRICULA (ValorCodigo, Codigo, Situacion, IdNinio, IdNivelDetalle, IdTutor, InstitucionProcedencia, EsRepitente, Activo, FechaRegistro)
                VALUES ((SELECT ISNULL(MAX(ValorCodigo), 0) + 1 FROM MATRICULA), 
                        CONCAT('MAT', (SELECT ISNULL(MAX(ValorCodigo), 0) + 1 FROM MATRICULA)),
                        @Situacion, @IdNinio, @IdNivelDetalle, @IdTutor, @InstitucionProcedencia, @EsRepitente, 1, GETDATE());

                UPDATE NIVEL_DETALLE
                SET VacantesDisponibles = VacantesDisponibles - 1,
                    VacantesOcupadas = VacantesOcupadas + 1
                WHERE IdNivelDetalle = @IdNivelDetalle;

                COMMIT TRANSACTION;
            END
            ELSE
            BEGIN
                THROW 51000, 'No hay vacantes disponibles en el nivel seleccionado.', 1;
            END
        END TRY
        BEGIN CATCH
            ROLLBACK TRANSACTION;
            DECLARE @ErrorMessage NVARCHAR(4000);
            DECLARE @ErrorSeverity INT;
            DECLARE @ErrorState INT;

            SELECT @ErrorMessage = ERROR_MESSAGE(),
                   @ErrorSeverity = ERROR_SEVERITY(),
                   @ErrorState = ERROR_STATE();

            RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
        END CATCH;
        """, id_ninio, id_nivel_detalle, id_tutor, situacion, institucion_procedencia, es_repitente)
        conn.commit()
        messagebox.showinfo("Éxito", "Proceso de matriculación completado exitosamente.")
    except pyodbc.Error as e:
        conn.rollback()
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def ejecutar_automatizacion(entry_id_ninio, entry_id_nivel_detalle, entry_id_tutor, entry_situacion, entry_institucion_procedencia, var_es_repitente):
    id_ninio = int(entry_id_ninio.get())
    id_nivel_detalle = int(entry_id_nivel_detalle.get())
    id_tutor = int(entry_id_tutor.get())
    situacion = entry_situacion.get()
    institucion_procedencia = entry_institucion_procedencia.get()
    es_repitente = var_es_repitente.get()

    automatizar_matricula(id_ninio, id_nivel_detalle, id_tutor, situacion, institucion_procedencia, es_repitente)
