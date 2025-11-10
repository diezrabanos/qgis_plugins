#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para reemplazar placeholders de capturas en Guia_Usuario_Silvilidar.html
Uso: python reemplazar_capturas.py
"""

import os
import re
from pathlib import Path

def reemplazar_capturas(html_file, screenshots_dir):
    """
    Reemplaza los placeholders de capturas con las imágenes reales.

    Args:
        html_file: Ruta del archivo HTML
        screenshots_dir: Ruta de la carpeta con las capturas
    """

    if not os.path.exists(html_file):
        print(f"❌ Error: Archivo {html_file} no encontrado")
        return False

    if not os.path.exists(screenshots_dir):
        print(f"❌ Error: Carpeta {screenshots_dir} no encontrada")
        print(f"ℹ️  Crea la carpeta con: mkdir {screenshots_dir}")
        return False

    # Leer el archivo HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Mapeo de placeholders a archivos
    placeholders = {
        'screenshots/01_ventana_principal.png': 'Ventana principal del plugin',
        'screenshots/02_dialogo_parametros.png': 'Diálogo de parámetros',
        'screenshots/02b_dialogo_proyectar.png': 'Diálogo de proyección',
        'screenshots/02c_dialogo_salida.png': 'Diálogo de salida',
        'screenshots/02d_dialogo_similares.png': 'Diálogo de búsqueda similares',
        'screenshots/03_qgis_capa_vectorial.png': 'QGIS con capa vectorial',
        'screenshots/04_procesamiento_en_curso.png': 'Ventana de progreso',
        'screenshots/05_resultado_hm.png': 'Raster HM en QGIS',
        'screenshots/05b_resultado_fcc.png': 'Raster FCC en QGIS',
        'screenshots/05c_resultado_hbc.png': 'Raster HBC en QGIS',
        'screenshots/05d_resultado_rc.png': 'Raster RC en QGIS',
        'screenshots/06_teselas_clasificadas.png': 'Teselas clasificadas',
        'screenshots/07_zonas_similares.png': 'Zonas similares',
        'screenshots/08_histograma_similitud.png': 'Histograma de similitud',
        'screenshots/09_carpeta_salida.png': 'Estructura de carpeta',
    }

    reemplazos = 0
    no_encontradas = []

    print("=" * 70)
    print("🔄 Reemplazando placeholders de capturas...")
    print("=" * 70)

    for archivo, descripcion in placeholders.items():
        ruta_completa = os.path.join(screenshots_dir, os.path.basename(archivo))

        if os.path.exists(ruta_completa):
            # Buscar y reemplazar el placeholder
            patron = rf'<small>\(Reemplazar con: {re.escape(archivo)}\)</small>'
            reemplazo = f'<img src="{archivo}" alt="{descripcion}">'

            if re.search(patron, contenido):
                contenido = re.sub(patron, reemplazo, contenido)
                reemplazos += 1
                print(f"✓ Reemplazado: {archivo}")
            else:
                print(f"⚠ Placeholder no encontrado para: {archivo}")
        else:
            print(f"✗ Imagen no encontrada: {ruta_completa}")
            no_encontradas.append(archivo)

    # Guardar el archivo actualizado
    if reemplazos > 0:
        copia_seguridad = html_file + ".backup"
        os.rename(html_file, copia_seguridad)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(contenido)

        print("=" * 70)
        print(f"✓ {reemplazos} placeholder(s) reemplazado(s)")
        print(f"📁 Archivo guardado: {html_file}")
        print(f"📁 Copia de seguridad: {copia_seguridad}")
        print("=" * 70)

        if no_encontradas:
            print("\n⚠️  Imágenes faltantes:")
            for img in no_encontradas:
                print(f"  - {img}")

        return True
    else:
        print("❌ No se realizaron reemplazos. Verifica que los archivos existan.")
        return False

def listar_capturas_existentes(screenshots_dir):
    """
    Lista las capturas encontradas en la carpeta.
    """
    if not os.path.exists(screenshots_dir):
        print(f"Carpeta no encontrada: {screenshots_dir}")
        return

    archivos = sorted([f for f in os.listdir(screenshots_dir) if f.endswith('.png')])

    if not archivos:
        print(f"No hay imágenes PNG en: {screenshots_dir}")
        return

    print(f"\n📸 Capturas encontradas en {screenshots_dir}:")
    print("-" * 50)
    for archivo in archivos:
        ruta = os.path.join(screenshots_dir, archivo)
        tamaño = os.path.getsize(ruta) / 1024  # KB
        print(f"  ✓ {archivo:<40} ({tamaño:.1f} KB)")
    print("-" * 50)

if __name__ == "__main__":
    # Configuración
    dir_script = Path(__file__).parent
    html_file = dir_script / "Guia_Usuario_Silvilidar.html"
    screenshots_dir = dir_script / "screenshots"

    print("\n" + "=" * 70)
    print("📸 REEMPLAZADOR DE CAPTURAS - Silvilidar")
    print("=" * 70 + "\n")

    # Listar capturas existentes
    listar_capturas_existentes(str(screenshots_dir))

    # Realizar reemplazos
    print()
    reemplazar_capturas(str(html_file), str(screenshots_dir))

    print("\n✓ Proceso completado. Abre el HTML en tu navegador para verificar.")

