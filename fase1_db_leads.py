# ==============================================================================
# PROYECTO: Lead Generation Bot (Yelp Scraper)
# DESCRIPCIÓN: Fase 1 - Configuración de Base de Datos para Prospectos
# DESCRIPTION: Phase 1 - Prospect Database Configuration
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import sqlite3

def crear_base_de_datos():
    """
    Crea la base de datos y la tabla de leads si no existen.
    Creates the database and the leads table if they do not exist.
    """
    try:
        # Conexión inicial al archivo de base de datos SQLite
        # Initial connection to the SQLite database file
        conn = sqlite3.connect('prospectos_negocios.db')
        cursor = conn.cursor()

        # Definición de la estructura de la tabla 'leads' con campos esenciales
        # Definition of the 'leads' table structure with essential fields
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_extraccion TEXT,
                negocio_nombre TEXT,
                categoria TEXT,
                telefono TEXT,
                sitio_web TEXT,
                ubicacion TEXT,
                rating REAL
            )
        ''')

        # Guardar cambios y cerrar la conexión
        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print("✅ [EXITO/SUCCESS] Base de datos 'prospectos_negocios.db' lista / ready.")

    except Exception as e:
        print(f"❌ [ERROR] No se pudo crear la base de datos / Could not create database: {e}")

if __name__ == "__main__":
    crear_base_de_datos()