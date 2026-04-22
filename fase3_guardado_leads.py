# ==============================================================================
# PROYECTO: Lead Generation Bot (Yelp Scraper)
# DESCRIPCIÓN: Fase 3 - Extracción y Guardado en Base de Datos (SQLite)
# DESCRIPTION: Phase 3 - Extraction and Database Storage (SQLite)
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import sqlite3
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def iniciar_browser():
    """Configuración del navegador / Browser configuration."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def guardar_en_db(nombre, categoria, ubicacion):
    """
    Guarda un lead en la base de datos evitando duplicados.
    Saves a lead to the database while avoiding duplicates.
    """
    try:
        conn = sqlite3.connect('prospectos_negocios.db')
        cursor = conn.cursor()

        # Validación de duplicados para mantener la integridad de los datos
        # Duplicate validation to maintain data integrity
        cursor.execute("SELECT id FROM leads WHERE negocio_nombre = ?", (nombre,))
        existe = cursor.fetchone()

        if not existe:
            fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                INSERT INTO leads (fecha_extraccion, negocio_nombre, categoria, ubicacion)
                VALUES (?, ?, ?, ?)
            ''', (fecha_hoy, nombre, categoria, ubicacion))
            conn.commit()
            print(f"✅ Guardado / Saved: {nombre}")
        else:
            print(f"⏭️ Omitido (Ya existe) / Skipped (Already exists): {nombre}")

        conn.close()
    except Exception as e:
        print(f"❌ Error al guardar en DB / Error saving to DB: {e}")

def ejecutar_fase_3(driver, categoria, ciudad):
    """
    Orquestación de búsqueda y persistencia de datos.
    Search orchestration and data persistence.
    """
    print(f"🔍 Buscando '{categoria}' en '{ciudad}'...")
    driver.get("https://www.yelp.com")
    time.sleep(random.uniform(4, 6))

    try:
        search_find = driver.find_element(By.CSS_SELECTOR, "input#search_description, input#find_desc")
        search_near = driver.find_element(By.CSS_SELECTOR, "input#search_location, input#dropperText_pi_6c11")
        search_find.send_keys(categoria)
        search_near.send_keys(Keys.CONTROL + "a")
        search_near.send_keys(Keys.DELETE)
        search_near.send_keys(ciudad)
        search_near.send_keys(Keys.ENTER)
    except:
        pass

    print("\n🚨 Resuelve el Captcha y presiona ENTER / Solve Captcha and press ENTER...")
    input("👉 Esperando resultados / Waiting for results...")

    # Extracción y Guardado Directo / Direct Extraction and Storage
    resultados = driver.find_elements(By.CSS_SELECTOR, "h3 a")
    for res in resultados:
        nombre_lead = res.text.strip()
        if nombre_lead and "biz" in res.get_attribute("href"):
            # Integración con la base de datos
            # Database integration
            guardar_en_db(nombre_lead, categoria, ciudad)

if __name__ == "__main__":
    browser = iniciar_browser()
    ejecutar_fase_3(browser, "Dentists", "Atlanta")
    browser.quit()
    print("\n🚀 Fase 3 finalizada. Leads seguros en la DB / Leads secure in DB!")