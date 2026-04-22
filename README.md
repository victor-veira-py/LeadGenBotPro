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
