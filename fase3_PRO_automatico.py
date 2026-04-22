# ==============================================================================
# PROYECTO: Lead Generation Bot (Yelp Scraper)
# DESCRIPCIÓN: Fase 3 PRO - Automatización Total (Sin intervención manual)
# DESCRIPTION: Phase 3 PRO - Total Automation (No manual intervention)
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import undetected_chromedriver as uc
import sqlite3
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


def iniciar_browser_invisible():
    """
    Inicia un motor de navegación avanzado que evade la detección de bots.
    Starts an advanced navigation engine that evades bot detection.
    """
    print("🚀 Iniciando motor de navegación invisible / Starting invisible engine...")
    options = uc.ChromeOptions()
    # Mantenemos la ventana visible para evitar bloqueos agresivos de Yelp
    # Keep the window visible to avoid aggressive Yelp blocks
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    return driver


def guardar_lead(nombre, categoria, ciudad, link):
    """
    Persistencia de datos avanzada incluyendo enlaces directos.
    Advanced data persistence including direct links.
    """
    conn = sqlite3.connect('prospectos_negocios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM leads WHERE negocio_nombre = ?", (nombre,))

    if not cursor.fetchone():
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Se mapea el link al campo 'sitio_web' para trazabilidad
        # Mapping the link to the 'sitio_web' field for traceability
        cursor.execute("""
            INSERT INTO leads (fecha_extraccion, negocio_nombre, categoria, ubicacion, sitio_web) 
            VALUES (?, ?, ?, ?, ?)
        """, (fecha, nombre, categoria, ciudad, link))
        conn.commit()
        print(f"✅ Lead con Link guardado / Lead with Link saved: {nombre}")
    conn.close()


def ejecutar_scraping_automatico(categoria, ciudad):
    """
    Flujo de trabajo 100% automatizado con simulación de comportamiento humano.
    100% automated workflow with human behavior simulation.
    """
    driver = iniciar_browser_invisible()

    try:
        driver.get("https://www.yelp.com")
        time.sleep(random.uniform(5, 8))

        # Localización de elementos de búsqueda / Locating search elements
        search_find = driver.find_element(By.CSS_SELECTOR, "input#search_description, input#find_desc")
        search_near = driver.find_element(By.CSS_SELECTOR, "input#search_location, input#dropperText_pi_6c11")

        # Simulación de escritura humana (letra por letra)
        # Human typing simulation (character by character)
        for letra in categoria:
            search_find.send_keys(letra)
            time.sleep(random.uniform(0.1, 0.3))

        time.sleep(1)

        search_near.send_keys(Keys.CONTROL + "a")
        search_near.send_keys(Keys.DELETE)

        for letra in ciudad:
            search_near.send_keys(letra)
            time.sleep(random.uniform(0.1, 0.3))

        search_near.send_keys(Keys.ENTER)

        print("⏳ Esperando carga automática / Waiting for auto-load...")
        time.sleep(10)

        # Extracción masiva de datos / Bulk data extraction
        resultados = driver.find_elements(By.CSS_SELECTOR, "h3 a")
        for res in resultados:
            nombre = res.text.strip()
            link = res.get_attribute("href")
            if nombre and "biz" in link:
                guardar_lead(nombre, categoria, ciudad, link)

    except Exception as e:
        print(f"⚠️ Error en el proceso / Process error: {e}")
    finally:
        print("\n🎯 Proceso terminado / Process finished.")
        driver.quit()


if __name__ == "__main__":
    # Ejemplo de ejecución autónoma / Autonomous execution example
    ejecutar_scraping_automatico("Roofing", "Orlando, FL")