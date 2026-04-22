# ==============================================================================
# PROYECTO: Lead Generation Bot (Yelp Scraper)
# DESCRIPCIÓN: Herramienta de visualización de datos en consola
# DESCRIPTION: Console data visualization tool
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import sqlite3

def mostrar_leads():
    """
    Consulta y muestra los registros principales almacenados en la base de datos.
    Queries and displays the main records stored in the database.
    """
    try:
        # Conexión a la base de datos de prospectos
        # Connection to the business leads database
        conn = sqlite3.connect('prospectos_negocios.db')
        cursor = conn.cursor()

        # Selección de campos clave para una vista rápida en consola
        # Selection of key fields for a quick console view
        cursor.execute("SELECT id, fecha_extraccion, negocio_nombre, ubicacion FROM leads")
        filas = cursor.fetchall()

        # Encabezados de la tabla con formato de alineación
        # Table headers with alignment formatting
        print(f"\n{'ID':<4} | {'FECHA / DATE':<20} | {'NEGOCIO / BUSINESS':<40} | {'UBICACIÓN / LOCATION'}")
        print("-" * 105)

        # Iteración y muestra de cada registro encontrado
        # Iteration and display of each record found
        for fila in filas:
            print(f"{fila[0]:<4} | {fila[1]:<20} | {fila[2]:<40} | {fila[3]}")

        # Cierre de conexión y resumen final
        # Connection closure and final summary
        conn.close()
        print(f"\n📊 Total de leads en la base de datos / Total leads in database: {len(filas)}")

    except Exception as e:
        print(f"❌ Error al leer la base de datos / Error reading database: {e}")

if __name__ == "__main__":
    mostrar_leads()