# ==============================================================================
# PROYECTO: Lead Generation Bot (Yelp Scraper)
# DESCRIPCIÓN: Fase 5 - Reporte Ejecutivo (Pandas + Estética Profesional)
# DESCRIPTION: Phase 5 - Executive Reporting (Pandas + Professional Aesthetics)
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import pandas as pd
import sqlite3
from datetime import datetime

def exportar_leads_hibrido_pro():
    """
    Genera un reporte Excel con estética azul empresarial, sin ID
    y ordenado alfabéticamente para una entrega profesional.
    Generates an Excel report with business blue aesthetics, without ID
    and sorted alphabetically for a professional delivery.
    """
    try:
        # 1. Conexión y Carga de datos / Connection and Data Loading
        conn = sqlite3.connect('prospectos_negocios.db')

        # Consulta SQL optimizada para orden alfabético
        # Optimized SQL query for alphabetical order
        query = """
                    SELECT fecha_extraccion, negocio_nombre, categoria, telefono, sitio_web, ubicacion 
                    FROM leads 
                    ORDER BY negocio_nombre ASC
                """
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            print("❌ No hay datos para exportar / No data to export.")
            return

        # --- RENOMBRAR COLUMNAS / RENAME COLUMNS ---
        df.columns = [
            'FECHA REGISTRO', 'NOMBRE DEL NEGOCIO',
            'CATEGORÍA', 'TELÉFONO', 'SITIO WEB REAL', 'UBICACIÓN'
        ]

        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        nombre_excel = f"Reporte_Final_Leads_{fecha_hoy}.xlsx"

        # 2. Exportación con Formato XlsxWriter / Export with XlsxWriter Format
        with pd.ExcelWriter(nombre_excel, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Leads Validados', index=False)

            workbook = writer.book
            worksheet = writer.sheets['Leads Validados']

            # --- DEFINICIÓN DE ESTILOS (Azul Empresarial) ---
            # --- STYLE DEFINITION (Business Blue) ---
            formato_header = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'vcenter',
                'align': 'center',
                'fg_color': '#003366', # Azul Oscuro / Dark Blue
                'font_color': 'white',
                'border': 1
            })

            formato_centrado = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1
            })

            formato_texto = workbook.add_format({
                'align': 'left',
                'valign': 'vcenter',
                'border': 1
            })

            # Aplicar formato a los encabezados / Apply format to headers
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, formato_header)

            # --- AJUSTE DE COLUMNAS / COLUMN ADJUSTMENT ---
            worksheet.set_column('A:A', 18, formato_centrado)  # FECHA
            worksheet.set_column('B:B', 45, formato_texto)     # NOMBRE
            worksheet.set_column('C:C', 15, formato_centrado)  # CATEGORÍA
            worksheet.set_column('D:D', 18, formato_centrado)  # TELÉFONO
            worksheet.set_column('E:E', 40, formato_texto)     # WEB
            worksheet.set_column('F:F', 30, formato_centrado)  # UBICACIÓN

            # Inmovilizar fila superior / Freeze top row
            worksheet.freeze_panes(1, 0)

        print(f"✅ ¡REPORTE GENERADO! / REPORT GENERATED!: {nombre_excel}")

    except Exception as e:
        print(f"❌ Error en la exportación / Export error: {e}")

if __name__ == "__main__":
    exportar_leads_hibrido_pro()