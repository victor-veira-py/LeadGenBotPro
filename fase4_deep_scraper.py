# ==============================================================================
# PROYECTO: Lead Generation Bot (Yelp Scraper)
# DESCRIPCIÓN: Fase 4 - Investigador PROFESIONAL (Extracción de Contactos)
# DESCRIPTION: Phase 4 - PROFESSIONAL Investigator (Contact Extraction)
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import sqlite3
import time
import random
import re


def actualizar_datos_finales(lead_id, telefono, web_real):
    """
    Guarda los datos enriquecidos en la DB asegurando la persistencia.
    Saves enriched data into the DB ensuring persistence.
    """
    try:
        conn = sqlite3.connect('prospectos_negocios.db')
        cursor = conn.cursor()

        # Limpieza de datos antes del guardado / Data cleaning before saving
        tel = telefono.strip() if telefono else "No encontrado"
        web = web_real.strip() if web_real else "No tiene sitio web"

        cursor.execute("""
            UPDATE leads 
            SET telefono = ?, sitio_web = ? 
            WHERE id = ?
        """, (tel, web, lead_id))

        conn.commit()  # Asegura que los datos estén listos para el Excel / Ensures data is ready for Excel
        conn.close()
        print(f"   💾 [DB] Datos asegurados para ID {lead_id} / Data secured for ID {lead_id}")
    except Exception as e:
        print(f"   ❌ [ERROR DB] No se pudo guardar / Could not save: {e}")


def investigar_leads_profundo():
    """
    Navega en los perfiles de Yelp para extraer teléfonos y sitios web reales.
    Navigates through Yelp profiles to extract phone numbers and real websites.
    """
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    # Patrón Regex para identificar números de teléfono de USA
    # Regex pattern to identify USA phone numbers
    patron_tel = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}')

    try:
        conn = sqlite3.connect('prospectos_negocios.db')
        cursor = conn.cursor()

        # Seleccionamos registros que necesitan enriquecimiento de datos
        # Selecting records that need data enrichment
        cursor.execute("""
            SELECT id, negocio_nombre, sitio_web 
            FROM leads 
            WHERE (telefono IS NULL OR telefono = '' OR sitio_web LIKE '%yelp.com%')
            LIMIT 15
        """)
        pendientes = cursor.fetchall()
        conn.close()

        if not pendientes:
            print("✅ No hay leads pendientes de investigación / No leads pending investigation.")
            return

        for l_id, nombre, url_yelp in pendientes:
            print(f"🔎 Investigando / Investigating: {nombre}")
            try:
                driver.get(url_yelp)
                time.sleep(random.uniform(7, 10))

                # --- EXTRACCIÓN DE TELÉFONO / PHONE EXTRACTION ---
                elementos = driver.find_elements(By.XPATH, "//*[contains(text(), '(')]")
                telefono = "No encontrado"
                for el in elementos:
                    texto = el.text.strip()
                    if patron_tel.search(texto):
                        telefono = patron_tel.search(texto).group()
                        break

                # --- EXTRACCIÓN DE WEB REAL / REAL WEB EXTRACTION ---
                try:
                    elemento_web = driver.find_element(By.XPATH, "//a[contains(@href, '/biz_redir')]")
                    raw_url = elemento_web.get_attribute("href")
                    # Decodificación de la URL de redirección de Yelp
                    # Decoding Yelp's redirection URL
                    web_real = raw_url.split("url=")[1].split("&")[0].replace("%3A", ":").replace("%2F",
                                                                                                  "/") if "url=" in raw_url else elemento_web.text
                except:
                    web_real = "No tiene sitio web"

                # Guardado en base de datos / Saving to database
                actualizar_datos_finales(l_id, telefono, web_real)
                print(f"   ✨ Encontrado / Found: {telefono} | {web_real}")

                time.sleep(random.uniform(5, 8))

            except Exception as e:
                print(f"   ⚠️ Error con / Error with {nombre}: {e}")
                continue

    except Exception as e:
        print(f"❌ Error general / General error: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    investigar_leads_profundo()