# ==============================================================================
# PROYECTO: Lead Generation Bot (Yelp Scraper)
# DESCRIPCIÓN: Fase 2 - Extracción de Nombres y Enlaces tras Búsqueda
# DESCRIPTION: Phase 2 - Extraction of Names and Links after Search
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


def iniciar_browser():
    """
    Configura e inicia el navegador con opciones anti-detección.
    Configures and starts the browser with anti-detection options.
    """
    options = Options()
    # Desactiva el flag de automatización para evitar bloqueos
    # Disables the automation flag to avoid blocks
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver


def buscar_en_yelp(driver, categoria, ubicacion):
    """
    Realiza la búsqueda de nicho y ciudad en el portal de Yelp.
    Performs the niche and city search on the Yelp portal.
    """
    print(f"🔍 Buscando '{categoria}' en '{ubicacion}'...")
    driver.get("https://www.yelp.com")
    time.sleep(random.uniform(3, 5))

    try:
        # Selectores para los campos de búsqueda (Descripción y Ubicación)
        # Selectors for search fields (Description and Location)
        search_find = driver.find_element(By.CSS_SELECTOR, "input#search_description, input#find_desc")
        search_near = driver.find_element(By.CSS_SELECTOR, "input#search_location, input#dropperText_pi_6c11")

        search_find.send_keys(categoria)
        time.sleep(1)

        # Limpieza del campo de ubicación antes de escribir
        # Clearing the location field before typing
        search_near.send_keys(Keys.CONTROL + "a")
        search_near.send_keys(Keys.DELETE)
        search_near.send_keys(ubicacion)
        search_near.send_keys(Keys.ENTER)

    except Exception as e:
        print(f"⚠️ Error al interactuar con los buscadores / Error interacting with search fields: {e}")


def extraer_datos_pantalla(driver):
    """
    Extrae los nombres y enlaces de los negocios visibles en los resultados.
    Extracts the names and links of the businesses visible in the results.
    """
    print("\n--- 📋 LISTA DE PROSPECTOS ENCONTRADOS / LIST OF FOUND LEADS ---")

    # Buscamos los títulos de los negocios vinculados a sus perfiles
    # Looking for business titles linked to their profiles
    resultados = driver.find_elements(By.CSS_SELECTOR, "h3 a")

    conteo = 0
    for res in resultados:
        nombre = res.text.strip()
        enlace = res.get_attribute("href")

        # Filtramos para asegurar que sean enlaces de negocios reales
        # Filtering to ensure they are real business links
        if nombre and "biz" in enlace:
            conteo += 1
            print(f"{conteo}. NEGOCIO: {nombre}")
            print(f"   LINK: {enlace[:60]}...")

    if conteo == 0:
        print("❌ No se detectaron prospectos. Revisa el Captcha / No leads detected. Check Captcha.")


if __name__ == "__main__":
    browser = iniciar_browser()
    # Ejemplo de búsqueda inicial
    # Initial search example
    buscar_en_yelp(browser, "Dentists", "Miami, FL")

    # --- INTERVENCIÓN HUMANA / HUMAN INTERVENTION ---
    print("\n🚨 ESPERA: Si ves un Captcha en Chrome, resuélvelo manualmente.")
    input("👉 Cuando veas la lista de negocios en Chrome, presiona [ENTER] aquí para extraer...")

    extraer_datos_pantalla(browser)

    print("\n✅ Fase 2 completada con éxito / Phase 2 successfully completed.")
    browser.quit()