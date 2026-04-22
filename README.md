# 🗄️ Phase 1: SQLite Database Configuration | Fase 1: Configuración de Base de Datos

[English](#english) | [Español](#español)

---

## English
This script initializes the local storage system for the **Yelp Lead Generation Bot**. It uses **SQLite** to ensure data persistence, allowing the system to store and organize commercial leads efficiently without complex servers.

### ✨ Key Technical Features:
* **Automated Creation:** If the database file doesn't exist, the script creates it instantly.
* **Optimized Schema:** Includes essential fields for Lead generation: Business Name, Category, Phone, Website, Location, and Rating.
* **Data Integrity:** Configured with `IF NOT EXISTS` clauses to prevent accidental overwriting of existing tables.

---

## Español
Este script inicializa el sistema de almacenamiento local para el **Bot de Generación de Leads de Yelp**. Utiliza **SQLite** para garantizar la persistencia de los datos, permitiendo almacenar y organizar prospectos comerciales de manera eficiente sin servidores externos.

### ✨ Características Técnicas:
* **Creación Automatizada:** Si el archivo de la base de datos no existe, el script lo genera instantáneamente.
* **Esquema Optimizado:** Incluye campos esenciales para la generación de leads: Nombre del negocio, Categoría, Teléfono, Sitio Web, Ubicación y Rating.
* **Integridad de Datos:** Configurado con cláusulas `IF NOT EXISTS` para evitar la sobrescritura accidental de tablas existentes.

---
🛠️ Extra Utilities | Utilidades Extra
ver_leads.py: A quick-access script to preview the SQLite database directly from the terminal. | Un script de acceso rápido para previsualizar la base de datos SQLite directamente desde la terminal.

---
---

# 🤖 Phase 2: Dynamic Web Scraper (Selenium) | Fase 2: Scraper Dinámico (Selenium)

[English](#english-f2) | [Español](#español-f2)

---

## English
This stage focuses on real-time data extraction using **Selenium WebDriver**. The bot simulates human browsing behavior to bypass basic security and capture business names and profile links directly from Yelp.

### ✨ Key Features:
* **Anti-Detection Measures:** Configured with custom User-Agents and automation flags removal to minimize blocking risks.
* **Human-in-the-Loop:** Designed to allow manual captcha resolution before proceeding with data extraction.
* **Dynamic Search:** Parameters for niche (category) and location are fully customizable within the script.

---

## Español
Esta etapa se enfoca en la extracción de datos en tiempo real usando **Selenium WebDriver**. El bot simula la navegación humana para evadir seguridad básica y capturar nombres de negocios y enlaces de perfiles directamente desde Yelp.

### ✨ Características Técnicas:
* **Medidas Anti-Detección:** Configurado con User-Agents personalizados y eliminación de flags de automatización para minimizar riesgos de bloqueo.
* **Intervención Humana:** Diseñado para permitir la resolución manual de captchas antes de proceder con la extracción de datos.
* **Búsqueda Dinámica:** Los parámetros de nicho (categoría) y ubicación son totalmente personalizables dentro del script.

---
---

# 🗄️ Phase 3: Data Persistence & Duplicate Control | Fase 3: Persistencia de Datos y Control de Duplicados

[English](#english-f3) | [Español](#español-f3)

---

## English
This phase bridges the gap between web scraping and professional data management. The system now automatically saves extracted leads into the SQLite database, ensuring data consistency and reliability.

### ✨ Key Features:
* **Duplicate Prevention:** Implements SQL queries to verify if a business already exists before inserting, preventing redundant data.
* **Timestamping:** Every record is stored with a precise extraction date and time for future auditing.
* **Automated Workflow:** Seamlessly connects the Selenium extraction layer with the SQLite storage layer.

---

## Español
Esta fase cierra la brecha entre el web scraping y la gestión de datos profesional. El sistema ahora guarda automáticamente los leads extraídos en la base de datos SQLite, asegurando la consistencia y confiabilidad de la información.

### ✨ Características Técnicas:
* **Prevención de Duplicados:** Implementa consultas SQL para verificar si un negocio ya existe antes de insertarlo, evitando datos redundantes.
* **Marca de Tiempo:** Cada registro se almacena con la fecha y hora exacta de extracción para futuras auditorías.
* **Flujo Automatizado:** Conecta sin problemas la capa de extracción de Selenium con la capa de almacenamiento de SQLite.

---
---

# ⚡ Phase 3 PRO: Full Automation Mode | Fase 3 PRO: Modo Automatización Total

[English](#english-pro) | [Español](#español-pro)

---

## English
This "PRO" version upgrades the scraper to a fully autonomous system. It eliminates the need for manual intervention by using advanced anti-detection drivers and simulating human-like typing patterns.

### ✨ Advanced Features:
* **Undetected ChromeDriver:** Integrated `undetected-chromedriver` to bypass sophisticated bot detection systems.
* **Human-like Typing:** Simulates character-by-character typing with random delays to mimic organic user behavior.
* **Extended Data Capture:** Automatically captures the direct Yelp profile link for each lead, enriching the database for further extraction.

---

## Español
Esta versión "PRO" eleva el scraper a un sistema totalmente autónomo. Elimina la necesidad de intervención manual mediante el uso de controladores anti-detección avanzados y la simulación de patrones de escritura humana.

### ✨ Características Avanzadas:
* **Undetected ChromeDriver:** Integra `undetected-chromedriver` para evadir sistemas sofisticados de detección de bots.
* **Escritura Humana:** Simula la escritura carácter por carácter con retrasos aleatorios para imitar el comportamiento de un usuario orgánico.
* **Captura de Datos Extendida:** Captura automáticamente el enlace directo al perfil de Yelp de cada lead, enriqueciendo la base de datos para extracciones futuras.

---
---

# 🔍 Phase 4: Deep Data Extraction | Fase 4: Extracción Profunda de Datos

[English](#english-f4) | [Español](#español-f4)

---

## English
This module performs a detailed investigation by visiting each individual Yelp profile stored in the database. Its goal is to extract direct contact information, bypassing Yelp's internal links to find the business's actual phone number and official website.

### ✨ Key Features:
* **Regex Phone Detection:** Uses Regular Expressions to accurately identify and extract US-formatted phone numbers from the page source.
* **URL Decoding:** Implements logic to decode Yelp's redirection links (`/biz_redir`), extracting the clean, direct URL of the business's official website.
* **Smart Update:** Uses SQL `UPDATE` commands with `COMMIT` to ensure data persistence, enriching existing records without creating duplicates.

---

## Español
Este módulo realiza una investigación detallada visitando cada perfil individual de Yelp almacenado en la base de datos. Su objetivo es extraer información de contacto directo, evadiendo los enlaces internos de Yelp para encontrar el número de teléfono real y el sitio web oficial del negocio.

### ✨ Características Técnicas:
* **Detección de Teléfono con Regex:** Utiliza Expresiones Regulares para identificar y extraer con precisión números de teléfono con formato de EE. UU. desde el código fuente de la página.
* **Decodificación de URL:** Implementa lógica para decodificar los enlaces de redirección de Yelp (`/biz_redir`), extrayendo la URL limpia y directa del sitio web oficial del negocio.
* **Actualización Inteligente:** Utiliza comandos SQL `UPDATE` con `COMMIT` para garantizar la persistencia de los datos, enriqueciendo los registros existentes sin crear duplicados.
